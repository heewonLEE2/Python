# 📋 Python Flask ToDo List

간단하고 실용적인 웹 기반 할 일 관리 애플리케이션입니다. Flask를 사용하여 제작되었으며, 직관적인 인터페이스로 할 일을 쉽게 추가하고 삭제할 수 있습니다.

## ✨ 주요 기능

- ✅ **할 일 추가**: 새로운 작업을 간편하게 추가
- 🗑️ **할 일 삭제**: 완료된 작업을 목록에서 제거
- 📱 **반응형 디자인**: 모바일과 데스크톱 모두 지원
- 🔄 **실시간 업데이트**: 페이지 새로고침 없이 목록 관리

## 🛠️ 기술 스택

- **Backend**: Python 3.x, Flask 3.1.1
- **Frontend**: HTML5, Jinja2 템플릿
- **데이터 저장**: 메모리 기반 (개발용)

## 📁 프로젝트 구조

```
Todo_List_project/
├── app.py              # Flask 메인 애플리케이션
├── requirements.txt    # Python 패키지 의존성
├── templates/
│   └── index.html     # 메인 웹 페이지 템플릿
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

1. **할 일 추가**: 입력 필드에 작업 내용을 입력하고 "추가하기" 버튼 클릭
2. **할 일 삭제**: 각 항목 옆의 "삭제 버튼"을 클릭하여 완료된 작업 제거
3. **목록 확인**: 현재 등록된 모든 할 일을 한눈에 확인

## 🔧 주요 구현 사항

### Flask 라우트
- `GET /`: 메인 페이지 렌더링 및 할 일 목록 표시
- `POST /add`: 새로운 할 일 추가
- `POST /delete/<task_id>`: 특정 할 일 삭제

### 데이터 구조
```python
todo_item = {
    'id': 1,           # 고유 식별자
    'task': '할 일',    # 작업 내용
    'done': False      # 완료 상태 (향후 확장용)
}
```

## 🎯 향후 개선 계획

- [ ] **데이터베이스 연동**: SQLite 또는 PostgreSQL 사용
- [ ] **할 일 완료 기능**: 체크박스를 통한 완료 상태 관리
- [ ] **할 일 수정 기능**: 기존 작업 내용 편집
- [ ] **카테고리 분류**: 작업을 카테고리별로 분류
- [ ] **우선순위 설정**: 중요도에 따른 작업 정렬
- [ ] **사용자 인증**: 개인별 할 일 관리
- [ ] **CSS 스타일링**: 더 아름다운 UI/UX 디자인

## 👨‍💻 개발자

- **작성자**: [heewonLEE]
- **이메일**: [gmldnjs1616@gmail.com]

---

⭐ 이 프로젝트가 도움이 되었다면 별표를 눌러주세요!