# tut_5.py
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
#add
from st_aggrid.shared import GridUpdateMode

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

shows = pd.read_csv("netflix_titles.csv")
gb = GridOptionsBuilder.from_dataframe(shows)

# ---
gb.configure_selection(selection_mode="multiple", use_checkbox=True)

gridOptions = gb.build()


data = AgGrid(shows, 
              gridOptions=gridOptions, 
              enable_enterprise_modules=True, 
              allow_unsafe_jscode=True, 
              update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write(data["selected_rows"])

# streamlit run tut_5.py
# stop: ctrl + c 
