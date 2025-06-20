import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 한글 폰트 적용
import matplotlib.font_manager as fm
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()
plt.rcParams["axes.unicode_minus"] = False

# 데이터 불러오기
df = pd.read_csv("data/Sleep_health_and_lifestyle_dataset.csv")

# 제목
st.title("🛌 수면 건강 분석 대시보드")

# 시각화 1: 수면장애 vs 수면시간
st.subheader("수면장애별 수면 시간 분포")
fig1, ax1 = plt.subplots()
sns.boxplot(data=df, x="Sleep Disorder", y="Sleep Duration", ax=ax1)
ax1.set_title("수면장애에 따른 수면 시간", fontproperties=font_prop)
st.pyplot(fig1)

# 성별 평균 수면시간
st.subheader("성별 평균 수면 시간")
fig2, ax2 = plt.subplots()
sns.barplot(data=df, x="Gender", y="Sleep Duration", ax=ax2)
ax2.set_title("성별 수면 시간", fontproperties=font_prop)
st.pyplot(fig2)