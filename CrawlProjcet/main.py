import os
from dotenv import load_dotenv
from openai import OpenAI
from pymongo import MongoClient
from fastapi import FastAPI

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

# /recommend 로 get 요청이 들어왔을때 처리할 함수
@app.get("/recommend")
def recommend(title: str = None, keyword: str="파이썬"):
    if not title:
        return {"error":"title 파라미터가 누락되었습니다."}
    
    books = list(collection.find({"검색어":keyword}))
    if not books:
        print(f"'{keyword}'에 대한 MongoDB 데이터가 없음 -> 크롤링 시작")