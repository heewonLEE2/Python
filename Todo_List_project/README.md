# 📋 Python Flask ToDo List

간단하고 실용적인 웹 기반 할 일 관리 애플리케이션입니다. Flask를 사용하여 제작되었으며, 직관적인 인터페이스로 할 일을 쉽게 추가하고 삭제할 수 있습니다.

## ✨ 주요 기능

- ✅ **할 일 추가**: 새로운 작업을 간편하게 추가 (마감일 설정 가능)
- 🗑️ **할 일 삭제**: 완료된 작업을 목록에서 제거
- ✔️ **완료 상태 토글**: 체크박스로 완료/미완료 상태 변경
- 🔍 **필터링**: 전체/완료/미완료 작업별 분류 보기
- 📅 **정렬 기능**: 마감일 기준 오름차순/내림차순 정렬
- 💾 **데이터 영속성**: SQLite 데이터베이스로 데이터 영구 저장
- 📱 **반응형 디자인**: Bootstrap 5 기반 모바일/데스크톱 지원

## 🛠️ 기술 스택

- **Backend**: Python 3.x, Flask 3.1.1, Flask-SQLAlchemy 3.1.1
- **Frontend**: HTML5, Jinja2 템플릿, Bootstrap 5
- **데이터베이스**: SQLite (개발용)
- **ORM**: SQLAlchemy

## 📁 프로젝트 구조

```
Todo_List_project/
├── app.py              # Flask 메인 애플리케이션
├── requirements.txt    # Python 패키지 의존성
├── templates/
│   └── index.html     # 메인 웹 페이지 템플릿 (Bootstrap 5 적용)
├── todo.db            # SQLite 데이터베이스 파일 (실행 후 생성)
└── venv/              # 가상환경 (선택사항)
```

## 🚀 설치 및 실행 방법

### 1. 저장소 클론
```bash
git clone [your-repository-url]
cd Todo_List_project
```

### 2. 가상환경 생성 및 활성화 (권장)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python app.py
```

### 5. 브라우저에서 접속
```
http://localhost:5000
```

## 💡 사용 방법

1. **할 일 추가**: 
   - 입력 필드에 작업 내용을 입력
   - 선택적으로 마감일 설정 가능
   - "추가하기" 버튼 클릭으로 저장

2. **할 일 관리**:
   - ✅ **완료 버튼**: 작업 완료 상태로 변경 (취소 가능)
   - 🗑️ **삭제 버튼**: 작업을 영구적으로 제거

3. **필터링 및 정렬**:
   - **전체/완료/미완료** 버튼으로 작업 상태별 필터링
   - **마감일 ↑/↓** 버튼으로 날짜순 정렬

4. **데이터 관리**:
   - 모든 데이터는 SQLite 데이터베이스에 자동 저장
   - 서버 재시작 후에도 데이터 유지

## 🔧 주요 구현 사항

### Flask 라우트
- `GET /`: 메인 페이지 렌더링 및 할 일 목록 표시 (필터링/정렬 지원)
- `POST /add`: 새로운 할 일 추가 (마감일 포함)
- `POST /delete/<task_id>`: 특정 할 일 삭제
- `POST /toggle/<task_id>`: 할 일 완료 상태 토글

### 데이터베이스 모델
```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)        # 고유 식별자
    task = db.Column(db.String(100), nullable=False)    # 작업 내용
    done = db.Column(db.Boolean, default=False)         # 완료 상태
    due_date = db.Column(db.Date, nullable=True)        # 마감일 (선택)
```

### 주요 기능 구현
- **필터링**: URL 쿼리 파라미터로 상태별 필터 (`?filter=done/undone/all`)
- **정렬**: 마감일 기준 오름차순/내림차순 정렬 (`?sort=asc/desc`)
- **상태 토글**: AJAX 없이 서버 사이드 처리로 완료 상태 변경

## 🎯 향후 개선 계획

- [x] **데이터베이스 연동**: SQLite 데이터베이스 구현 완료 ✅
- [x] **할 일 완료 기능**: 체크박스를 통한 완료 상태 관리 완료 ✅
- [x] **필터링 기능**: 완료/미완료/전체 상태별 필터링 완료 ✅
- [x] **정렬 기능**: 마감일 기준 정렬 기능 완료 ✅
- [x] **마감일 설정**: 할 일 추가 시 마감일 설정 기능 완료 ✅
- [x] **UI 개선**: Bootstrap 5 적용으로  디자인 완료 ✅
- [ ] **할 일 수정 기능**: 기존 작업 내용 편집
- [ ] **카테고리 분류**: 작업을 카테고리별로 분류
- [ ] **우선순위 설정**: 중요도에 따른 작업 정렬
- [ ] **사용자 인증**: 개인별 할 일 관리
- [ ] **알림 기능**: 마감일 임박 알림
- [ ] **통계 대시보드**: 완료율, 생산성 통계

⭐ 이 프로젝트가 도움이 되었다면 별표를 눌러주세요!

## 👨‍💻 개발자

- **작성자**: [heewonLEE]
- **이메일**: [gmldnjs1616@gmail.com]

---

⭐ 이 프로젝트가 도움이 되었다면 별표를 눌러주세요!