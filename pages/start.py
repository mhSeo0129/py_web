import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# 전체 페이지 설정
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=200)

def main():
    # 유저한테 입력을 받는 방법

    # 1. 이름 입력 받기
    name = st.text_input('당신의 닉네임을 입력하세요!')

    if name != '':
        st.subheader(name + '님, 안녕하세요!')

        if 'user_name' not in st.session_state:
            st.session_state['user_name'] = ''
        st.session_state['user_name'] = name

    # 2. 입력 글자 갯수 제한
    budget = st.number_input('오늘의 식단 예산을 입력하세요', 0, 20000)
    height = st.number_input('키를 입력하세요', 0, 200)
    weight = st.number_input('몸무게를 입력하세요', 0, 150)
    st.session_state['budget'] = budget

    # 시작하기 버튼을 가운데 정렬하는 컨테이너 추가
    button_container = st.container()

    selected_categories = st.multiselect('구성할 음식 종류를 모두 선택하세요!!!', ['라면', '김밥', '빵', '커피', '탄산음료', '유제품', '이온음료', '아이스크림', '디저트', '과자'])

    # Streamlit 세션 상태에 선택한 값을 저장
    st.session_state['selected_categories'] = selected_categories

if __name__ == "__main__":
    main()
    
    # 중앙 하단 버튼
    if st.button("식단 구성하기"):
        # 버튼을 눌렀을 때의 동작
        switch_page('menu')
