# app.py

import streamlit as st
import pandas as pd

# 전체 페이지 설정
st.set_page_config(page_title="와라, 편의점", page_icon="🍱", layout="wide")

# 왼쪽 상단 로고 (크기 조절)
st.image("logo.png", use_column_width=False, width=300)  # 로고 크기를 조절하려면 width 값을 조절하세요.

# 중앙에 텍스트 (가운데 정렬)
st.title("자취생을 위한 건강한 한끼")
st.write("## st.write 사용")

# 중앙 하단 버튼
if st.button("식단 구성하기"):
    # 버튼을 눌렀을 때의 동작
    st.success("식단이 생성되었습니다. 맛있게 드세요!")

if st.button("click button"):
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
    
    
# 다중선택박스
st.subheader("\n다중선택박스")
multi_select = st.multiselect('Please select somethings in multi selectbox!',
                            ['A', 'B', 'C', 'D'])

st.write('You selected:', multi_select)

#슬라이더

st.subheader("슬라이더")
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.success("Success")

def main() :
    df = pd.read_csv('cvs_db.csv') # CSV 파일 불러오고 df 변수에 저장

    st.dataframe(df)

    df.head()

    st.dataframe( df.head() )
    st.write( df.head() )

if __name__ == '__main__' :
    main()