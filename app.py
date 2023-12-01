import streamlit as st
data = [1114, 1234, 423]
st.write('# Hello World')
st.write('\n## raw')
data
st.write('## bar chart')
st.bar_chart(data)
import pandas as pd
sview = pd.Series(data)
sview