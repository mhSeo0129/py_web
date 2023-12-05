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

min_price_list = []

for i in range(len(data_set)):
    min_price_list.append(find_min_cost(data_set[i]))

budget = int(input("사용가능한 예산을 입력해주세요: "))

choice_index_list = [0, 2, 4]

min_sum = 0
for i in choice_index_list:
    min_sum += min_price_list[i]

# dp table 만들기
dp = []

#dp table 만드는 함수
def make_dp_table(choice_index_list, budget):
    number = len(choice_index_list)
    print(number)
    print(budget)
    print(min_sum)
    for _ in range(number * 20):
        dp.append([[0] * number] * (int((budget - min_sum)/100) + 1))

make_dp_table(choice_index_list, budget)


print(data_set[0][0][3])
print(data_set[0][1][3])
print(data_set[0][2][3])
print(min_price_list)
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

            # ========여기부터
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
                
dp_each_category(0, 0)
dp_each_category(2, 1)
dp_each_category(4, 2)

print(dp[59][20])

# for i in range(0, 20):
#     cost = min_sum
#     for j in range(0, 21):
#         if i != 0:
#             dp[i][j] = dp[i-1][j]
        
#         if cost < min_price_list[2] + min_price_list[4] + data_set[0][i][3]:
#             cost += 100
#             continue
#         else:
#             if dp[i][j][0] == 0 or dp[i][j][0][12] < data_set[0][i][12]:
#                 dp[i][j][0] = data_set[0][i]
#             cost += 100

# for i in range(20, 40):
#     cost = min_sum
#     for j in range(0, 21):

#         dp[i][j] = dp[i-1][j]
        
#         if cost < dp[i][j][0][3] + min_price_list[4] + data_set[2][i-20][3]:
#             cost += 100
#             continue
#         else:
#             if dp[i][j][1] == 0 or dp[i][j][1][12] < data_set[2][i-20][12]:
#                 dp[i][j][1] = data_set[2][i-20]
#             cost += 100

# for i in range(40, 60):
#     cost = min_sum
#     for j in range(0, 21):

#         dp[i][j] = dp[i-1][j]
        
#         if cost < dp[i][j][0][3] + dp[i][j][1][3] + data_set[4][i-40][3]:
#             cost += 100
#             continue
#         else:
#             if dp[i][j][2] == 0 or dp[i][j][2][12] < data_set[4][i-40][12]:
#                 dp[i][j][2] = data_set[4][i-40]
#             cost += 100

# print(dp)