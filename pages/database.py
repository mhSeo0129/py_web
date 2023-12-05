import streamlit as st
import pandas as pd

# 전체 페이지 설정
st.set_page_config(page_title="음식 목록", page_icon="🍱", layout="wide")

with open("../pages/style.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

if 'user_name' in st.session_state:
    name = st.session_state['user_name']
    st.subheader(name + "님, 음식 목록 페이지에 오신 것을 환영합니다!")
    

st.subheader("각 종류별로 선택해서 모든 데이터 확인할 수 있도록")

def main() :
    df = pd.read_csv('cvs_db.csv')

    with st.expander('모든 음식 확인하기') :
        st.dataframe(df)

if __name__ == "__main__" :
    main()
