# tut1.py

import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

#　csvが保存されているパスを指定する
shows = pd.read_csv("netflix_titles.csv")  

AgGrid(shows)

# streamlit run tut_1.py
# stop: ctrl + c 