# GPT 기반 교보문고 도서 추천 시스템

교보문고에서 도서 정보를 크롤링하고, GPT를 활용하여 개인화된 도서 추천을 제공하는 웹 애플리케이션입니다.

## 프로젝트 구조

```
├── crawler.py      # 교보문고 크롤링 모듈
├── main.py         # FastAPI 백엔드 서버
├── gradio_app.py   # Gradio 웹 인터페이스
└── images/         # 크롤링한 책 이미지 저장 폴더
```

## 주요 기능

### 🔍 도서 검색 및 크롤링

- 교보문고에서 키워드 기반 도서 검색
- 책 제목, 저자, 가격, 출판사, 출판일 정보 수집
- 책 표지 이미지 자동 다운로드 및 저장
- MongoDB에 크롤링 데이터 저장

### 🤖 GPT 기반 도서 추천

- OpenAI GPT-4를 활용한 지능형 도서 추천
- 선택한 책과 유사한 주제/스타일의 책 3권 추천
- 각 추천에 대한 상세한 이유 제공

## 기술 스택

- **Backend**: FastAPI, Python
- **Database**: MongoDB
- **Web Scraping**: Selenium, BeautifulSoup
- **AI**: OpenAI GPT-4 API
- **Frontend**: Gradio
- **Image Processing**: Pillow (PIL)

## 설치 및 실행

### 1. 의존성 설치

```bash
pip install fastapi uvicorn pymongo selenium beautifulsoup4 openai gradio pillow python-dotenv webdriver-manager requests
```

### 2. 환경 변수 설정

`.env` 파일을 생성하고 다음 정보를 입력하세요:

```env
API_KEY=your_openai_api_key
MONGODB=your_mongodb_connection_string
```

### 3. 애플리케이션 실행

```bash
# 1. FastAPI 서버 실행 (포트 8000)
uvicorn main:app --reload

# 2. Gradio 웹 인터페이스 실행
python gradio_app.py
```

## API 엔드포인트

### GET /books

- **파라미터**: `keyword` (검색할 키워드)
- **기능**: 키워드로 도서 검색, 데이터가 없으면 자동 크롤링
- **반환**: 도서 목록 (JSON 배열)

### GET /recommend

- **파라미터**: `title` (책 제목), `keyword` (검색 키워드)
- **기능**: 선택한 책 기반 GPT 추천 생성
- **반환**: 추천 내용 및 이미지 경로

## 사용 방법

1. 웹 인터페이스에서 원하는 키워드 입력 (예: "파이썬", "소설" 등)
2. "도서 목록 불러오기" 버튼 클릭
3. 드롭다운에서 관심 있는 책 선택
4. "GPT 추천 받기" 버튼 클릭하여 개인화된 추천 받기

## 데이터베이스 스키마

MongoDB에 저장되는 도서 정보:

```json
{
  "검색어": "파이썬",
  "책제목": "책 제목",
  "저자": "저자명",
  "가격": "가격 정보",
  "출판사": "출판사명",
  "출판일": "출간일",
  "이미지저장경로": "로컬 이미지 경로",
  "판매사이트명": "Kyobo"
}
```

## 주요 특징

- **자동 크롤링**: 검색 데이터가 없으면 실시간으로 교보문고 크롤링
- **이미지 관리**: 책 표지 이미지 자동 다운로드 및 로컬 저장
- **에러 처리**: 크롤링 및 API 호출 시 안정적인 예외 처리
- **확장성**: MongoDB를 통한 대용량 데이터 처리 가능

## 주의사항

- OpenAI API 키가 필요합니다
- MongoDB 연결이 필요합니다
- 크롤링 시 교보문고 서버에 부하를 주지 않도록 적절한 딜레이 권장
- Chrome 브라우저가 시스템에 설치되어 있어야 합니다 (Selenium 사용)
