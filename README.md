# 🐍 Python 학습 및 프로젝트 저장소

Python 언어를 활용한 다양한 학습 자료와 실습 프로젝트들을 모아놓은 저장소입니다. 기초부터 실전 프로젝트까지 체계적으로 정리되어 있습니다.

## 📂 프로젝트 구조

```
Python/
├── Todo_List_project/     # Flask 기반 할 일 관리 웹 애플리케이션
├── OpenAI_API_project/    # OpenAI API를 활용한 LLM 서비스
├── CrawlProject/          # 교보문고 크롤링 & GPT 도서 추천 시스템
└── README.md             # 이 파일
```

## 🚀 주요 프로젝트

### 1. 📋 Todo List Project

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

### 2. 🤖 OpenAI API Project

**OpenAI API를 활용한 LLM 서비스**

- **기술 스택**: Python, OpenAI API
- **주요 기능**: 대화형 AI 서비스 구현
- **학습 목표**: API 연동, 인공지능 서비스 개발
- **상세 정보**: 각 프로젝트 폴더 내 문서 참조

### 3. 📚 교보문고 크롤링 & GPT 도서 추천 시스템

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

## 📚 학습 내용

### Python 기초

- 변수와 데이터 타입
- 제어 구조 (조건문, 반복문)
- 함수와 클래스
- 모듈과 패키지

### 웹 개발

- Flask 프레임워크
- FastAPI 프레임워크
- HTML 템플릿 엔진 (Jinja2)
- HTTP 메소드 (GET, POST)
- 라우팅과 뷰 함수

### 데이터베이스

- SQLAlchemy ORM (관계형 DB)
- MongoDB (NoSQL)
- SQLite 데이터베이스 연동
- 데이터 모델링 및 CRUD 연산

### 웹 크롤링 & 데이터 수집

- Selenium을 이용한 동적 페이지 크롤링
- BeautifulSoup을 이용한 HTML 파싱
- 이미지 다운로드 및 파일 관리
- 웹사이트 구조 분석 및 데이터 추출

### API 개발 & 연동

- RESTful API 설계 및 구현
- 외부 API 연동 (OpenAI GPT-4)
- JSON 데이터 처리
- 에러 핸들링 및 예외 처리

### 인공지능 & 머신러닝

- OpenAI GPT API 활용
- AI 기반 추천 시스템 구현
- 자연어 처리 응용

### 실전 프로젝트

- 웹 애플리케이션 구축
- 데이터베이스 연동
- 사용자 인터페이스 설계
- 배포 및 운영

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

## 📖 학습 가이드

### 1. 초보자를 위한 학습 순서

1. **Python 기초 문법** 학습
2. **Todo List Project**로 웹 개발 입문 (Flask + SQLite)
3. **OpenAI API Project**로 AI 서비스 개발 체험
4. **크롤링 & 추천 시스템**으로 고급 기술 통합 (FastAPI + MongoDB + AI)

### 2. 각 프로젝트 실습 방법

1. 해당 프로젝트 폴더로 이동
2. README.md 파일의 설치 가이드 따라하기
3. 코드 분석 및 기능 확장 시도
4. 개인 프로젝트로 응용 발전

### 3. 단계별 학습 목표

- **1단계**: 기본 웹 애플리케이션 개발 (Todo List)
- **2단계**: AI API 연동 및 활용 (OpenAI Project)
- **3단계**: 데이터 수집부터 AI 추천까지 종합 (크롤링 프로젝트)

## 🎯 학습 목표

- **웹 개발 기초**: Flask/FastAPI를 이용한 백엔드 개발 이해
- **데이터베이스 활용**: SQLAlchemy ORM 및 MongoDB를 통한 데이터 관리
- **웹 크롤링**: Selenium과 BeautifulSoup을 활용한 데이터 수집
- **AI 서비스 개발**: OpenAI API를 활용한 지능형 서비스 구현
- **API 활용**: 외부 서비스와의 연동 방법 습득
- **프로젝트 구조**: 실무에서 사용하는 코드 구조 학습
- **문제 해결**: 실제 문제를 코드로 해결하는 능력 향상
- **풀스택 개발**: 프론트엔드부터 백엔드, 데이터베이스까지 통합 개발

## 🏆 프로젝트별 난이도

| 프로젝트             | 난이도   | 주요 학습 내용                   |
| -------------------- | -------- | -------------------------------- |
| Todo List            | ⭐⭐     | Flask 기초, SQLite, 웹 개발 입문 |
| OpenAI API           | ⭐⭐⭐   | API 연동, AI 서비스 개발         |
| 크롤링 & 추천 시스템 | ⭐⭐⭐⭐ | 크롤링, NoSQL, AI 통합, 풀스택   |

## 🤝 기여 및 피드백

이 저장소는 Python 학습을 위한 개인 프로젝트 모음입니다. 질문이나 개선 제안이 있으시면 언제든 연락해주세요!

## 👨‍💻 개발자 정보

- **작성자**: heewonLEE
- **이메일**: gmldnjs1616@gmail.com
- **학습 목적**: Python 웹 개발 및 AI 서비스 개발

---

⭐ Python 학습 여정을 함께 해주셔서 감사합니다!
