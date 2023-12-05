import streamlit as st

# 전체 페이지 설정 (이 부분을 가장 위로 옮깁니다.)
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")


# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=300)


# 중앙에 텍스트 (가운데 정렬) 및 마진 추가
st.markdown("""
    <h2 style='text-align: center; margin-top: 50px; margin-bottom: 250px; color: black;'>
        자취생을 위한 건강한 한 끼
    </h2>
""", unsafe_allow_html=True)


# 중앙에 텍스트 (가운데 정렬)


sidebar_deco = st.sidebar.selectbox(
    'Pages',
    ('main', 'database', 'history', 'map', 'menu', 'practice', 'start'))

from streamlit_extras.switch_page_button import switch_page

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


# custom_css = f"""
#     @font-face {{
#         font-family: 'CustomFont';
#         src: url("./fonts/mhSeo.ttf") format("truetype");
#     }}

#     body {{
#         font-family: 'CustomFont', sans-serif;
#     }}
# """


# st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
