# import streamlit as st
# data = [1114, 1234, 423]
# st.write('# Hello World')
# st.write('\n## raw')
# data
# st.write('## bar chart')
# st.bar_chart(data)

# import pandas as pd
# sview = pd.Series(data)
# sview

# st.write('## Fuck You')

import streamlit as st

# 세션 상태 초기화
if 'user_text' not in st.session_state:
    st.session_state.user_text = ""

# Streamlit 앱 정의
def main():
    # 제목 추가
    st.title("Streamlit 글상자 예제")

    # 텍스트 상자 추가
    user_input = st.text_input("여기에 텍스트를 입력하세요:", "기본 텍스트")

    # 입력한 텍스트를 세션 상태에 저장
    st.session_state.user_text = user_input

    # 세션 상태에 저장된 텍스트 출력
    st.write("입력한 텍스트:", st.session_state.user_text)

if __name__ == "__main__":
    main()