import streamlit as st

# 전체 페이지 설정
st.set_page_config(page_title="식단 구성", page_icon="🍱", layout="wide")

if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''
else: 
    name = st.session_state['user_name']
    st.subheader(name + "님, 식단 구성 페이지에 오신 것을 환영합니다.")
