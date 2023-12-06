import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, add_page_title, show_pages

# 전체 페이지 설정 (가장 위로 이동)
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=200)

# 외부 CSS 파일을 불러오는 코드
external_css = """
<link rel="stylesheet" href="py_web/styles.css">
"""
st.markdown(external_css, unsafe_allow_html=True)

from st_pages import Page, add_page_title, show_pages

show_pages(
    [
        Page("main.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("pages/history.py", "History", ":books:"),
        # The pages appear in the order you pass them
        Page("pages/start.py", "Make menu", "🍘"),
        Page("pages/map.py", "map", "🛣️"),
        # Will use the default icon and name based on the filename if you don't
        # pass thems
        Page("pages/database.py", "All menu", "🧰"),
        Page("pages/menu.py", "your menu", "🥘")
    ]
)
st.markdown("""
<style>
.st-emotion-cache-j7qwjs eczjsme7{
    display: none;
}
</style>
""", unsafe_allow_html=True)


# 이미지 파일 경로
image_path = "subtitle.png"

# 이미지를 현재 열의 너비에 맞게 조정
st.image(image_path, use_column_width=True)


button_container = st.container()
with button_container:
    if st.button("시작하기"):
        switch_page('Make menu')

# 스타일을 적용하여 가운데 정렬
button_container.markdown("""
    <style>
        div.stButton {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)
