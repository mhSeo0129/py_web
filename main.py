import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# 전체 페이지 설정 (가장 위로 이동)
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=200)

# 외부 CSS 파일을 불러오는 코드
external_css = """
<link rel="stylesheet" href="py_web/styles.css">
"""
st.markdown(external_css, unsafe_allow_html=True)

# 이미지 파일 경로
image_path = "subtitle.png"

# 이미지를 현재 열의 너비에 맞게 조정
st.image(image_path, use_column_width=True)

# st.markdown("""
#     <h2 style='text-align: center; margin-top: 50px; margin-bottom: 250px; color: black;'>
#         자취생을 위한 건강한 한 끼
#     </h2>
# """, unsafe_allow_html=True)



# 중앙에 텍스트 (가운데 정렬)
sidebar_deco = st.sidebar.selectbox(
    'Pages',
    ('main', 'history', 'start', 'menu', 'database', 'map'))

button_container = st.container()
with button_container:
    if st.button("시작하기"):
        switch_page('start')

# 스타일을 적용하여 가운데 정렬
button_container.markdown("""
    <style>
        div.stButton {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)
