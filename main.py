# main.py

import streamlit as st
import pandas as pd

# 전체 페이지 설정
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=300)  # 로고 크기를 조절하려면 width 값을 조절하세요.

# 중앙에 텍스트 (가운데 정렬)
st.title("자취생을 위한 건강한 한끼")

sidebar_deco = st.sidebar.selectbox(
    'Pages',
    ('main', 'food categories', 'menu'))



st.link_button("시작하기", "http://localhost:8501/start")


# def switch_page(page_name: str):
#     from streamlit import _RerunData, _RerunException
#     from streamlit.source_util import get_pages

#     def standardize_name(name: str) -> str:
#         return name.lower().replace("_", " ")
    
#     page_name = standardize_name(page_name)

#     pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

#     for page_hash, config in pages.items():
#         if standardize_name(config["page_name"]) == page_name:
#             raise _RerunException(
#                 _RerunData(
#                     page_script_hash=page_hash,
#                     page_name=page_name,
#                 )
#             )

#     page_names = [standardize_name(config["page_name"]) for config in pages.values()]

#     raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
# from streamlit_extras.switch_page_button import switch_page

# if st.button("제발 돼라.."):
    # switch_page('history')
    
