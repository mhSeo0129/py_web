# app.py

import streamlit as st
import pandas as pd

# 전체 페이지 설정
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=300)  # 로고 크기를 조절하려면 width 값을 조절하세요.

# 중앙에 텍스트 (가운데 정렬)
st.title("자취생을 위한 건강한 한끼")

def main() :
    
    # 유저한테 입력을 받는 방법

    # 1. 이름 입력 받기
    name = st.text_input('이름을 입력하세요!')

    if name != '' :
        st.subheader(name + '님, 안녕하세요!')

    # 2. 입력 글자 갯수 제한
    height = st.text_input('키를 입력하세요', max_chars=10)
    st.subheader(height + "cm" )
    
if __name__ == "__main__" :
    main()


def main() :
    
    # 비밀번호 입력
    password = st.text_input('비밀번호 입력', type='password')
    st.write(password)

if __name__ == "__main__" :
    main()







# 중앙 하단 버튼
if st.button("식단 구성하기"):
    # 버튼을 눌렀을 때의 동작
    st.success("식단이 생성되었습니다. 맛있게 드세요!")


st.subheader("오늘 식단 구성은 어떻게 할까요?")
def main() :

    category = ['라면', '김밥', '빵', '커피', '탄산음료', '유제품', '이온음료', '아이스크림', '디저트', '과자']
    st.multiselect('구성할 음식 종류를 모두 선택하세요!', category)

if __name__ == "__main__" :
    main()

if st.button("\n\n\nclick button"):
      st.write("Data Loading..")
      # 데이터 로딩 함수는 여기에!

st.subheader("체크박스")
menu1 = st.checkbox('체크박스')

# 선택 박스

st.subheader("라디오버튼")
selected_item = st.radio("Radio Part", ("초콜릿", "딸기", "바나나", "멜론"))

if selected_item == "초콜릿":
    st.write("초콜릿")
elif selected_item == "딸기":
    st.write("딸기")
elif selected_item == "바나나":
    st.write("바나나")
elif selected_item == "멜론":
    st.write("멜론")



    
st.subheader("각 종류별로 선택해서 모든 데이터 확인할 수 있도록")

def main() :
    df = pd.read_csv('cvs_db.csv')

    with st.expander('모든 음식 확인하기') :
        st.dataframe(df)

if __name__ == "__main__" :
    main()



# def main() :
#     df = pd.read_csv('cvs_db.csv') # CSV 파일 불러오고 df 변수에 저장

#     st.dataframe(df)

#     df.head()

#     st.dataframe( df.head() )
#     st.write( df.head() )

# if __name__ == '__main__' :
#     main()


