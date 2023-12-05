import pandas as pd

db = pd.read_csv("cvs_db.csv")

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
def find_min_cost(data_list):
    3
    min = int(data_list[0][3][1:])
    for i in range(len(data_list)):
        if min > int(data_list[i][3][1:]):
            min = int(data_list[i][3][1:])
    return min

min_price_list = []

for i in range(len(data_set)):
    min_price_list.append(find_min_cost(data_set[i]))

print(min_price_list)