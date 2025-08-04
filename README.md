# Python 학습 및 프로젝트 저장소

Python 언어를 활용한 다양한 학습 자료와 실습 프로젝트들을 모아놓은 저장소입니다. 기초부터 실전 프로젝트까지 체계적으로 정리되어 있습니다.

## 🚀 주요 프로젝트

### 1. 🛌 수면 건강 분석 대시보드 (Streamlit)

🎬 **데모 영상 보기**: [YouTube 링크](https://youtu.be/Weq4QAWPQ6Q)

- **기술 스택**: Python, Streamlit, Plotly, Scikit-learn, OpenAI API
- **주요 기능**:
  - 📊 수면 데이터 기반 시각화 (박스플롯, 평균 수면 시간, 상관관계 히트맵 등)
  - 📈 회귀 분석 및 심박수 예측 기능
  - 💬 GPT 기반 수면·스트레스 관련 조언 제공
- **데이터셋**: Sleep_health_and_lifestyle_dataset.csv
- **실행 방법**: `streamlit run app.py`
- **상세 정보**: 본 README 하단에 전체 설명 포함

### 2. 📋 Todo List Project

**Flask 기반 웹 애플리케이션**

- **기술 스택**: Python 3.x, Flask 3.1.1, Flask-SQLAlchemy 3.1.1, Bootstrap 5
- **주요 기능**:
  - ✅ 할 일 추가/삭제 및 완료 상태 토글
  - 📅 마감일 설정 및 날짜순 정렬
  - 🔍 완료/미완료/전체 상태별 필터링
  - 💾 SQLite 데이터베이스 영구 저장
  - 📱 반응형 디자인 (모바일/데스크톱 지원)
- **학습 목표**: Flask 웹 프레임워크, SQLAlchemy ORM, 백엔드 개발 기초
- **상세 정보**: [Todo_List_project/README.md](./Todo_List_project/README.md)

### 3. 🤖 OpenAI API Project

**OpenAI API를 활용한 LLM 서비스**

- **기술 스택**: Python, OpenAI API
- **주요 기능**: 대화형 AI 서비스 구현
- **학습 목표**: API 연동, 인공지능 서비스 개발
- **상세 정보**: 각 프로젝트 폴더 내 문서 참조

### 4. 📚 교보문고 크롤링 & GPT 도서 추천 시스템

**웹 크롤링과 AI를 결합한 개인화 도서 추천 서비스**

- **기술 스택**: FastAPI, MongoDB, Selenium, BeautifulSoup, OpenAI GPT-4, Gradio
- **주요 기능**:
  - 🔍 교보문고 도서 정보 자동 크롤링 (제목, 저자, 가격, 출판사, 출판일)
  - 📖 책 표지 이미지 자동 다운로드 및 로컬 저장
  - 🤖 GPT-4 기반 개인화 도서 추천 (유사 도서 3권 + 추천 이유)
  - 💾 MongoDB를 통한 대용량 데이터 관리
  - 🌐 Gradio 기반 직관적인 웹 인터페이스
  - ⚡ FastAPI 백엔드 서버 (RESTful API)
- **학습 목표**: 웹 크롤링, NoSQL 데이터베이스, AI API 활용, 풀스택 개발
- **상세 정보**: [CrawlProject/README.md](./CrawlProject/README.md)

## 🛠️ 개발 환경 설정

### 필수 요구사항

- Python 3.7 이상
- pip (Python 패키지 관리자)
- Chrome 브라우저 (Selenium 사용)

### 권장 개발 도구

- **IDE**: VS Code, PyCharm
- **버전 관리**: Git
- **가상환경**: venv

### 공통 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate
```

## 🤝 기여 및 피드백

이 저장소는 Python 학습을 위한 개인 프로젝트 모음입니다. 질문이나 개선 제안이 있으시면 언제든 연락해주세요!

## 👨‍💻 개발자 정보

- **작성자**: heewonLEE
- **이메일**: gmldnjs1616@gmail.com
- **학습 목적**: Python 웹 개발 및 AI 서비스 개발

---

⭐ Python 학습 여정을 함께 해주셔서 감사합니다!
