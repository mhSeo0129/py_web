import streamlit as st

# 전체 페이지 설정
st.set_page_config(page_title="practice", page_icon="🍱", layout="wide")

st.markdown('## 이것은 제목입니다')
st.markdown('이것은 **굵은** 텍스트입니다')


with st.container():
    st.write('이것은 컨테이너 안에 있습니다')
    st.button('클릭')