import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.figure_factory as ff
import openai
import toml

# config/secrets.toml 파일 로드
secrets = toml.load("config/secrets.toml")

# API 키 가져오기
openai.api_key = secrets["openai"]["api_key"]


# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False
sns.set(style="whitegrid")

# 데이터 불러오기
df = pd.read_csv("data/Sleep_health_and_lifestyle_dataset.csv")
df[["Systolic", "Diastolic"]] = df["Blood Pressure"].str.split("/", expand=True).astype(int)

# 모델 학습 (한 번만 실행)
model = LinearRegression()
model.fit(df[["Sleep Duration", "Stress Level", "Quality of Sleep"]], df["Heart Rate"])

# 타이틀
st.title("🛌 수면 건강 분석 대시보드")

# 사이드바 구성
st.sidebar.header("📌 요약 정보")
# 요약 통계 출력
st.sidebar.write("샘플 수:", len(df))
st.sidebar.write("평균 수면 시간:", round(df["Sleep Duration"].mean(), 2))
st.sidebar.write("평균 스트레스 수준:", round(df["Stress Level"].mean(), 2))

# 선택 필터 예시 (직업별 필터링)
selected_job = st.sidebar.selectbox("직업 선택:", df["Occupation"].unique())
filtered_by_job = df[df["Occupation"] == selected_job]
st.sidebar.write(f"{selected_job} 직군의 평균 수면시간: {filtered_by_job['Sleep Duration'].mean():.2f}시간")

# 탭 생성
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 기본 시각화", "📈 상관관계 분석", "📉 회귀 분석", "🔮 심박수 예측", "💬 GPT 조언"])

# 📊 기본 시각화 탭
with tab1:
    st.subheader("수면장애별 수면 시간 분포 (Plotly)")
    fig1 = px.box(df, x="Sleep Disorder", y="Sleep Duration", color="Sleep Disorder")
    fig1.update_layout(title="수면장애에 따른 수면시간", title_font_family=font_prop.get_name())
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("성별 평균 수면 시간 (Plotly)")
    gender_avg = df.groupby("Gender")["Sleep Duration"].mean().reset_index()
    fig2 = px.bar(gender_avg, x="Gender", y="Sleep Duration", color="Gender", title="성별 평균 수면 시간")
    fig2.update_layout(title_font_family=font_prop.get_name())
    st.plotly_chart(fig2, use_container_width=True)

# 📈 상관관계 분석 탭
with tab2:
    st.subheader("생활 습관과 생체 지표 간 상관관계 (Plotly)")
    corr_cols = ["Sleep Duration", "Stress Level", "Quality of Sleep", "Systolic", "Diastolic", "Heart Rate"]
    corr_matrix_full = df[corr_cols].corr()

    fig3 = ff.create_annotated_heatmap(
        z=corr_matrix_full.values,
        x=list(corr_matrix_full.columns),
        y=list(corr_matrix_full.index),
        annotation_text=[[f"{val:.2f}" for val in row] for row in corr_matrix_full.values],
        colorscale="RdBu",
        showscale=True,
        reversescale=True
    )
    fig3.update_layout(title="생활 습관과 생체 지표 간 상관관계", title_font_family=font_prop.get_name())
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("수면 관련 변수 간 상관계수 (Plotly)")
    corr_df = df[["Sleep Duration", "Stress Level", "Quality of Sleep"]]
    corr_matrix_sleep = corr_df.corr()

    fig5 = ff.create_annotated_heatmap(
        z=corr_matrix_sleep.values,
        x=list(corr_matrix_sleep.columns),
        y=list(corr_matrix_sleep.index),
        annotation_text=[[f"{val:.2f}" for val in row] for row in corr_matrix_sleep.values],
        colorscale="RdBu",
        showscale=True,
        reversescale=True
    )
    fig5.update_layout(title="수면 관련 변수 간 상관계수", title_font_family=font_prop.get_name())
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("""
    ### 📌 그래프 해석 요약
    - 수면시간이 늘어날수록 스트레스는 감소하고 수면의 질은 향상되는 경향이 있습니다.
    - 스트레스와 수면의 질은 음의 상관관계를 보이며, 수면시간과 수면의 질은 양의 관계입니다.
    - 생체 지표인 심박수와 수축기/이완기 혈압도 생활 습관 변수와 일부 상관관계를 보여줍니다.
    """)

# 📉 회귀 분석 탭
with tab3:
    st.subheader("수면시간과 스트레스 수준의 관계 (Plotly 회귀선)")
    fig4 = px.scatter(df, x="Sleep Duration", y="Stress Level",
                      trendline="ols", color_discrete_sequence=["#1f77b4"],
                      title="수면시간 vs 스트레스 수준 회귀 분석")
    fig4.update_layout(title_font_family=font_prop.get_name(),
                       xaxis_title="수면시간", yaxis_title="스트레스 수준")
    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("""
    ### 📌 분석 요약  
    - 수면시간이 짧을수록 스트레스 수준이 높아지는 경향이 있습니다.  
    - 회귀선을 통해 이 관계가 선형적임을 시각적으로 확인할 수 있습니다.  
    - 충분한 수면이 스트레스 관리에 도움이 될 수 있음을 시사합니다.
    """)

with tab4:
    st.subheader("🔮 사용자 입력 기반 심박수 예측")

    sleep_input = st.number_input("수면 시간 (시간)", min_value=0.0, max_value=12.0, step=0.5, value=7.0)
    stress_input = st.slider("스트레스 수준 (1~10)", 1, 10, value=5)
    quality_input = st.slider("수면의 질 (1~10)", 1, 10, value=6)
    age_input = st.number_input("당신의 나이", min_value=10, max_value=100, step=1)

    if st.button("심박수 예측 + 분석"):
        user_input = [[sleep_input, stress_input, quality_input]]
        pred_heart = model.predict(user_input)[0]
        st.success(f"💡 예상 심박수는 약 {pred_heart:.1f} BPM입니다.")

        # 예측 결과 시각화
        fig_pred = px.bar(x=["예상 심박수"], y=[pred_heart], text=[f"{pred_heart:.1f} BPM"],
                          labels={"x": "항목", "y": "BPM"}, title="예측된 심박수")
        fig_pred.update_traces(textposition="outside")
        fig_pred.update_layout(yaxis_range=[40, 120], title_font_family=font_prop.get_name())
        st.plotly_chart(fig_pred, use_container_width=True)

        # 연령대 평균과 비교 분석
        same_age_group = df[(df["Age"] >= age_input - 2) & (df["Age"] <= age_input + 2)]
        if not same_age_group.empty:
            group_mean = same_age_group["Heart Rate"].mean()
            st.markdown(f"### 🧑‍🤝‍🧑 같은 연령대 평균 심박수: **{group_mean:.1f} BPM**")

            if pred_heart > group_mean + 5:
                st.warning("예측된 심박수가 같은 연령대 평균보다 **높습니다**. 스트레스나 활동 상태를 점검해보세요.")
            elif pred_heart < group_mean - 5:
                st.info("예측된 심박수가 같은 연령대 평균보다 **낮습니다**. 안정된 상태일 수 있어요.")
            else:
                st.success("예측된 심박수가 같은 연령대와 **비슷한 수준**입니다. 정상 범주로 보입니다.")
        else:
            st.info("입력한 나이와 유사한 연령대 데이터가 부족해 비교가 어려워요.")

# 💬 GPT 조언 탭
with tab5:
    st.subheader("💬 ChatGPT에게 건강 조언 받기")

    topic = st.selectbox("궁금한 주제를 선택하세요", [
        "스트레스 관리 팁", "수면의 질 향상 방법", "심박수 낮추는 방법", "건강한 수면 습관"
    ])

    if st.button("조언 요청하기"):
        with st.spinner("ChatGPT에게 조언을 요청하는 중..."):
            prompt = f"{topic}에 대해 구체적으로 3~5가지 생활 팁을 알려줘."

            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "당신은 스트레스 및 수면 건강 전문 컨설턴트입니다. 사용자에게 명확하고 간결한 번호 목록으로 조언을 제공하세요."},
                    {"role": "user", "content": prompt}
                ]
            )

            advice = response.choices[0].message.content
            st.markdown(f"🧠 **ChatGPT의 조언:**\n\n{advice}")