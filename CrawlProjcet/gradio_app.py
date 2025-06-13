import gradio as gr
import requests
import os
# 파이썬에서 이미지를 보여주기 위한 모듈
from PIL import Image

API_URL = "http://localhost:8000"

# 책 검색 함수
def get_titles(keyword):
    res = requests.get(f'{API_URL}/books', params={"keyword":keyword})
    if res.ok:
        # json 으로 데이터를 받아 books에 저장
        books = res.json()
        print(f'{len(books)}권 검색됨')
        # list 컴프리핸즈
        return [book["책제목"] for book in books if "책제목" in book]
    print("도서 목록 불러오기 실패")
    return []

# 책 추천 함수
def recommend_book(title, keyword):
    res = requests.get(f"{API_URL}/recommend", params={"title" : title, "keyword": keyword})
    data = res.json()
    img_path = data.get("image")
    img = Image.open(img_path) if img_path and os.path.exists(img_path) else None
    # 1 arg 이 false 면 2 arg
    return data.get("recommendation", "추천 실패"), img

# 책 검색 하고 추천해주는 함수
def search_and_recomment(keyword):
    titles = get_titles(keyword)
    if titles:
        print(f"검색어 '{keyword}'로 {len(titles)}개 책 제목 불러옴.")
        return gr.update(choices=titles, value=titles[0])
    print(f"검색어 '{keyword}'결과 없음.")
    return gr.update(choices=[], value=None)

# UI 꾸미기
with gr.Blocks() as app:
    gr.Markdown("## GPT 기반 교보문고 도서 추천기")
    keyword_input = gr.Textbox(label="검색어 입력", placeholder="예: 파이썬")
    search_btn = gr.Button("도서 목록 불러오기")
    title_dropdown = gr.Dropdown(label="도서 선택")
    recommend_btn = gr.Button("GPT 추천 받기")
    output_text = gr.Textbox(label="추천 결과")
    output_img = gr.Image(label="책 이미지")

    # 검색 버튼 클릭
    search_btn.click(fn=search_and_recomment, inputs=keyword_input, outputs=title_dropdown)
    # 추천 버튼 클릭
    recommend_btn.click(fn=recommend_book, inputs=[title_dropdown, keyword_input],
    outputs=[output_text, output_img])

app.launch()