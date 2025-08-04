from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# pip install fastapi
# pip install "uvicron[standard]"
# pip intall jinja2

app = FastAPI()

# 정적 파일 (JS, CSS 등) 제공
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML 템플릿 디렉토리
templates = Jinja2Templates(directory="templates")

# HTML 페이지 제공
@app.get("/", response_class=HTMLResponse)
async def get_page(request: Request):   # 사용자 request 정보
    return templates.TemplateResponse("index.html", {"request": request})

# 백엔드 API – JSON 데이터 제공
@app.get("/api/data")
async def get_data():
    return {"message": "FastAPI에서 보내는 데이터입니다."}
# 파이썬 안에서 우리는 딕셔너리를 사용하는 건데 FastApi 가 Json 형식으로 변환해서 response해준다.