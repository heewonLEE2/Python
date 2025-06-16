import os
from dotenv import load_dotenv
from openai import OpenAI
from pymongo import MongoClient
from fastapi import FastAPI
from crawler import crawl_kyobo

# env 파일을 읽어오기 위한 메소드
load_dotenv()
openai_client = OpenAI(api_key=os.getenv("API_KEY"))
mongo_client = MongoClient(os.getenv("MONGODB"))
app = FastAPI()

# 데이터 베이스 생성 및 컬랙션 연결(없으면 생성)
db = mongo_client['book_db']
collection = db['kyobo_books']

# /books 로 get 요청이 왔을 때 처리할 함수 데이터 베이스에서 검색
@app.get("/books")
def get_books(keyword: str= "파이썬") -> list[dict]:
    books = list(collection.find({"검색어":keyword}, {"_id":0}))
    print(f"'{keyword}' 검색 결과 개수 : {len(books)}")
    if not books:
        print(f"'{keyword}'에 대한 MongoDB 데이터가 없음 -> 크롤링 시작")
        crawl_kyobo(keyword, max_page=3)
        books = list(collection.find({"검색어" :keyword}, {"_id":0}))
        print(f'크롤링 후 {len(books)}건 저장됨')
    return books

def normalize(text):
    return text.replace("\n","").replace("\r","").strip().lower()

# /recommend 로 get 요청이 들어왔을때 처리할 함수
@app.get("/recommend")
def recommend(title: str = None, keyword: str="파이썬"):
    if not title:
        return {"error":"title 파라미터가 누락되었습니다."}
    
    books = list(collection.find({"검색어":keyword}))
    if not books:
        print(f"'{keyword}'에 대한 MongoDB 데이터가 없음 -> 크롤링 시작")
        crawl_kyobo(keyword, max_page=3)
        books = list(collection.find({"검색어":keyword}))
    
    book = next((b for b in books if normalize(b.get("책제목", ""))==normalize(title)),None)
    if not book:
        print("유사한 제목을 가진 책을 찾지 못했습니다.")
        return {"message": "책을 찾을 수 없습니다."}

    prompt = f"""
        책 제목 : {book['책제목']}
        저자 : {book['저자']}
        설명:{book['출판사']}에서 출간된 책입니다.
        위 책과 비슷한 주제나 스타일을 가진 추천 도서 3권을 제안해줘.
        각 추천에는 간단한 이유도 포함해줘. """
    
    try:
        response = openai_client.chat.completions.create(
            model = "gpt-4",
            messages=[
                {"role":"system", "content": "당신은 전문 서평가 입니다."},
                {"role": "user", "content": prompt}
            ]
        )
        print("GPT 응답 완료")
        content = response.choices[0].message.content
        return {
            "recommendation" : content,
            "image" : book.get("이미지 저장경로", None)
        }
    except Exception as e:
        print(f"GPT 추전 실패{e}")
        return {"error": str(e)}