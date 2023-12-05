import streamlit as st

# 전체 페이지 설정
st.set_page_config(page_title="practice", page_icon="🍱", layout="wide")

st.markdown('## 이것은 제목입니다')
st.markdown('이것은 **굵은** 텍스트입니다')


with st.container():
    st.write('이것은 컨테이너 안에 있습니다')
    st.button('클릭')
    
st.link_button("Go to main", "http://localhost:8501/")


img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
    
def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")

if st.button("제발 돼라.."):
    switch_page("start")