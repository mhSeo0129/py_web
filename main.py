import streamlit as st
import pandas as pd

# 전체 페이지 설정 (이 부분을 가장 위로 옮깁니다.)
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

with open("style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=300)

# 중앙에 텍스트 (가운데 정렬)
st.title("자취생을 위한 건강한 한끼")

sidebar_deco = st.sidebar.selectbox(
    'Pages',
    ('main', 'database', 'history', 'map', 'menu', 'practice', 'start'))

from streamlit_extras.switch_page_button import switch_page

if st.button("시작하기"):
    switch_page('start')

st.write("My name is jeongwoo Kim")

custom_css = {
    '@font-face': {
        'font-family': '"CustomFont"',
        'src': 'url("/fonts/mhSeo.ttf") format("truetype")'
    },

    '[class^="ag-"]:not([class^="ag-icon"])': {
        'font-family': '"CustomFont"'
    }
}