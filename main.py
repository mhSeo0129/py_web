# main.py

import streamlit as st
import pandas as pd

with open( ".\style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# 전체 페이지 설정
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=300)  # 로고 크기를 조절하려면 width 값을 조절하세요.

# 중앙에 텍스트 (가운데 정렬)
st.title("자취생을 위한 건강한 한끼")

sidebar_deco = st.sidebar.selectbox(
    'Pages',
    ('main', 'food categories', 'menu'))

from streamlit_extras.switch_page_button import switch_page

if st.button("시작하기"):
    switch_page('start')


