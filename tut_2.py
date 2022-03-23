# tut1.py
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

shows = pd.read_csv("netflix_titles.csv")

# ---
gb = GridOptionsBuilder.from_dataframe(shows)
gb.configure_pagination()
gridOptions = gb.build()

AgGrid(shows, gridOptions=gridOptions)

# streamlit run tut_2.py
# stop: ctrl + c 