import streamlit as st

# 전체 페이지 설정
st.set_page_config(page_title="식단 구성", page_icon="🍱", layout="wide")

# 중앙에 텍스트 (가운데 정렬)
st.markdown("""
    <h1 style='text-align: center; margin-top: 50px; margin-bottom: 50px; color: black;'>
        식단 구성
    </h1>
""", unsafe_allow_html=True)

if 'user_name' not in st.session_state:
    st.write("")
elif st.session_state['user_name'] == "":    
    st.write("")
else:
    name = st.session_state['user_name']
    st.markdown("[ " + name + "님 입력 정보 ] ")

budget = st.session_state.get('budget', [])
# Streamlit 세션 상태에서 선택한 값을 가져옴
selected_categories = st.session_state.get('selected_categories', [])

# 선택한 값 출력
st.write(f"예산: {budget}원")
st.write(f"선택한 음식 종류: {selected_categories}")

# 예산에 맞는 최고의 단백질 식단을 추천하는 부분을 st.markdown으로 수정
st.markdown("""
           <p style='margin-top: 50px; margin-bottom: 50px; color: black;'>
            [ 예산에 맞는 최고의 단백질 식단을 추천합니다 ]
            </p>
""", unsafe_allow_html=True)

import pandas as pd

db = pd.read_csv("cvs_db_dp.csv")

db_list = db.values.tolist()

data_set = []
temp_list = []

if db_list:
    for i in range(len(db_list)):
        if i == 0:
            temp_list.append(db_list[i])
        elif db_list[i][1] != db_list[i-1][1]:
            data_set.append(temp_list.copy())
            temp_list = [db_list[i]]
        else:
            temp_list.append(db_list[i])

    data_set.append(temp_list.copy())

# 0라면 1김밥 2빵 3커피 4탄산음료 5유제품 6이온음료 7아이스크림 8디저트 9과자

# 각 항목 별 최소금액 찾기 & 가격은 정수로, 단백질은 실수로 바꾸기
def find_min_cost(data_list):
    min = int(data_list[0][3])
    for i in range(len(data_list)):
        data_list[i][3] = int(data_list[i][3])
        data_list[i][12] = float(data_list[i][12])
        if min > data_list[i][3]:
            min = data_list[i][3]    
    return min

choice_index_list = []

con_list = ['라면', '김밥', '빵', '커피', '탄산음료', '유제품', '이온음료', '아이스크림', '디저트', '과자']
for i in range(len(con_list)):
    if con_list[i] in selected_categories:
        choice_index_list.append(i)

min_price_list = []

for i in range(len(data_set)):
    min_price_list.append(find_min_cost(data_set[i]))

min_sum = 0
for i in choice_index_list:
    min_sum += min_price_list[i]

# dp table 만들기
dp = []

#dp table 만드는 함수
def make_dp_table(choice_index_list, budget):
    number = len(choice_index_list)
    # print(number)
    # print(budget)
    # print(min_sum)
    for _ in range(number * 20):
        dp.append([[0] * number] * (int((budget - min_sum)/100) + 1))

make_dp_table(choice_index_list, budget)

def dp_each_category(category_index, order_index):
    c = category_index
    o = order_index
    column = int((budget - min_sum)/100) + 1
    for i in range(20 * o, 20 + 20 * o):
        cost = min_sum
        for j in range(0, column):
            if i != 0:
                dp[i][j] = dp[i-1][j]

            compare = 0

            for k in range(0, o):
                compare += dp[i][j][k][3]

            for k in range(o + 1, len(choice_index_list)):
                compare += min_price_list[choice_index_list[k]]
            compare += data_set[c][i - 20 * o][3]
            if cost < compare:
                cost += 100
                continue
            else:
                if dp[i][j][o] == 0 or dp[i][j][o][12] < data_set[c][i - 20 * o][12]:
                    dp[i][j][o] = data_set[c][i - 20 * o]
                cost += 100

for i in range(0, len(choice_index_list)):
    dp_each_category(choice_index_list[i], i)

x = len(choice_index_list) * 20 - 1
y = int((budget - min_sum)/100)

df = pd.DataFrame(dp[x][y], columns=["ID","종류","상품명","가격(원)","칼로리(kcal)","나트륨(mg)","탄수화물(g)","당류(g)","지방(g)","트랜스지방(g)","포화지방(g)","콜레스테롤(mg)","단백질(g)"])

df_without_first_column = df.drop(columns=['ID'])

st.table(df_without_first_column)

total_cost = df["가격(원)"].sum()
total_cal = df["칼로리(kcal)"].sum()
total_protein = df["단백질(g)"].sum()

weight = st.session_state['weight']
weight = int(weight)

st.write(f"총 가격: {total_cost}원")
st.write(f"총 칼로리: {total_cal}kcal")
st.write(f"총 단백질: {total_protein}g")

st.write(f"건강한 성인의 경우 일반적으로 체중 1kg 당 0.8g에서 1.2g의 단백질이 권장됩니다.")

st.markdown(name + "님의 권장 단백질 섭취량은 " + str(int(0.8*weight)) + "~" + str(int(1.2*weight)) + "g 입니다.")
