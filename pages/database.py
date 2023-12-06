import streamlit as st
import pandas as pd

# 전체 페이지 설정
st.set_page_config(page_title="음식 목록", page_icon="🍱", layout="wide")

if 'user_name' in st.session_state:
    name = st.session_state['user_name']
    # st.subheader(name + "님, 음식 목록 페이지에 오신 것을 환영합니다!")

st.subheader("음식 목록")

# 라면
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '라면']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('라면 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 김밥
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '김밥']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('김밥 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()

# 빵
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '빵']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('빵 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
    
# 커피
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '커피']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('커피 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 탄산음료
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '탄산음료']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('탄산음료 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 유제품
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '유제품']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('유제품 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 이온음료
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '이온음료']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('이온음료 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 아이스크림
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '아이스크림']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('아이스크림 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 디저트
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '디저트']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('디저트 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()
    
# 과자
def main():
    df = pd.read_csv('cvs_db.csv')

    # 종류가 '라면'인 상품만 필터링하여 표시
    ramen_df = df[df['종류'] == '과자']

    # 행 번호를 1부터 시작하도록 설정
    ramen_df.index = range(1, len(ramen_df) + 1)

    # 1열 삭제
    ramen_df = ramen_df.drop(columns=[ramen_df.columns[0]])

    with st.expander('과자 상품 확인하기'):
        st.dataframe(ramen_df)

if __name__ == "__main__":
    main()