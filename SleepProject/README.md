# 🛌 수면 건강 분석 대시보드

> 이 프로젝트는 수면과 관련된 건강 데이터를 기반으로, 다양한 시각화와 예측 기능을 제공하는 **Streamlit 기반 대시보드**입니다.  
> 심박수 예측, 상관분석, 회귀분석 등 데이터 분석 기능과 함께 OpenAI의 ChatGPT API를 활용한 **건강 조언** 기능도 포함되어 있습니다.

🎬 **데모 영상 보기**: [YouTube 링크](https://youtu.be/Weq4QAWPQ6Q)

---

## 🗂 프로젝트 구조

```
📁 프로젝트 루트
├── app.py                           # Streamlit 대시보드 메인 파일
├── data/
│   └── Sleep_health_and_lifestyle_dataset.csv  # 수면 건강 관련 데이터셋
├── config/
│   └── secrets.toml                 # OpenAI API 키가 저장된 보안 설정 파일
└── README.md
```

---

## 🚀 실행 방법

1. **필수 라이브러리 설치**

```bash
pip install -r requirements.txt
```

2. **OpenAI API 키 설정**

- `config/secrets.toml` 파일 생성 후 아래와 같이 작성:

```toml
[openai]
api_key = "your-openai-api-key"
```

3. **Streamlit 앱 실행**

```bash
streamlit run app.py
```

---

## 🧠 주요 기능 소개

### 📊 기본 시각화

- 수면장애, 성별, 직업군에 따른 수면 시간 분석
- Plotly 기반 상호작용형 차트 제공

### 📈 상관관계 분석

- 수면 습관, 스트레스, 혈압, 심박수 간의 관계 시각화
- 히트맵을 통한 변수 간 상관계수 확인

### 📉 회귀 분석

- 수면 시간과 스트레스 간의 선형 회귀 분석
- 수면 시간의 중요성에 대한 시각적 이해 제공

### 🔮 심박수 예측

- 사용자의 수면 시간, 스트레스 수준, 수면 질 입력 → 심박수 예측
- 연령대 평균과 비교하여 상태 진단

### 💬 ChatGPT 조언

- OpenAI GPT-3.5 기반 조언 기능
- 스트레스, 수면 질, 건강한 습관 등에 대해 맞춤형 팁 제공

---

## 📊 사용된 데이터셋

- **Sleep_health_and_lifestyle_dataset.csv**
- 수면 시간, 스트레스 수준, 혈압, 심박수, 수면장애 등 12개 이상의 건강 관련 변수 포함

---

## 💼 사용 기술 스택

- **Python**: 데이터 분석 및 웹 프레임워크
- **Streamlit**: 대시보드 UI 구현
- **Pandas / Scikit-learn**: 데이터 처리 및 회귀 분석
- **Seaborn / Matplotlib / Plotly**: 시각화
- **OpenAI API**: GPT-3.5 기반 조언 생성

---
