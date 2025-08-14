import streamlit as st
import pandas as pd
import altair as alt

# 데이터 정의
data = {
    "월": [
        "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06",
        "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12"
    ],
    "매출액": [
        12000000, 13500000, 11000000, 18000000, 21000000, 24000000,
        22500000, 23000000, 19500000, 25000000, 26500000, 28000000
    ],
    "전년동월": [
        10500000, 11200000, 12800000, 15200000, 18500000, 20100000,
        19000000, 20500000, 18000000, 21500000, 23000000, 25000000
    ]
}

# 데이터프레임 생성 및 증감률 계산
df = pd.DataFrame(data)
df["증감률 (%)"] = ((df["매출액"] - df["전년동월"]) / df["전년동월"]) * 100

# 제목 출력
st.title("📊 월별 매출 대시보드")
st.subheader("2024년 매출 및 전년 동월 대비 분석")

# 라인 차트 시각화용 데이터 변환
df_melted = df.melt(id_vars="월", value_vars=["매출액", "전년동월"],
                    var_name="매출 구분", value_name="금액")

# 차트 생성
chart = alt.Chart(df_melted).mark_line(point=True).encode(
    x=alt.X("월:N", title="월"),
    y=alt.Y("금액:Q", title="금액 (원)"),
    color="매출 구분:N",
    tooltip=["월", "매출 구분", "금액"]
).properties(
    width=700,
    height=400,
    title="월별 매출 및 전년동월 비교"
)

# 차트 출력
st.altair_chart(chart, use_container_width=True)

# 데이터프레임 출력
st.markdown("### 📄 원시 데이터 테이블")
st.dataframe(df.style.format({
    "매출액": "{:,}",
    "전년동월": "{:,}",
    "증감률 (%)": "{:.1f}"
}), use_container_width=True)
