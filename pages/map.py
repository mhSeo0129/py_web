import numpy as np
import pandas as pd 
import streamlit as st
import requests

# 전체 페이지 설정
st.set_page_config(page_title="전국 편의점 지도", page_icon="🍱", layout="wide")


if 'user_name' in st.session_state:
    name = st.session_state['user_name']
    st.subheader(name + "님, 음식 목록 페이지에 오신 것을 환영합니다!")
    
#지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
base_position =  [37.5073423, 127.0572734]
#중심점의 위도, 경도 좌표를 리스트에 담습니다.

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 :lat  경도 lon으로 지정하였습니다. 


map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position , 
    columns=['lat', 'lon'])
# map data 생성 : 위치와 경도 

print(map_data)

st.code('st.map(map_data)')
# 웹사이트에 어떤 코드인지 표시해주기 
st.subheader('Map of Data ')
# 제목 생성 
st.map(map_data)
# 지도 생성 