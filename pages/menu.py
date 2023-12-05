import streamlit as st

# 전체 페이지 설정
st.set_page_config(page_title="식단 구성", page_icon="🍱", layout="wide")

# 중앙에 텍스트 (가운데 정렬)
st.markdown("""
    <h1 style='text-align: center; margin-top: 50px; margin-bottom: 50px; color: black;'>
        식단 구성
    </h1>
""", unsafe_allow_html=True)

budget = st.session_state.get('budget', [])
# Streamlit 세션 상태에서 선택한 값을 가져옴
selected_categories = st.session_state.get('selected_categories', [])

# 선택한 값 출력
st.write(f"예산: {budget}")
st.write(f"선택한 음식 종류: {selected_categories}")