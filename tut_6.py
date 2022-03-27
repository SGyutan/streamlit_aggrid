# tut_6.py
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

# st.write(data["selected_rows"])

# add
import plotly_express as px

selected_rows = data["selected_rows"]
selected_rows = pd.DataFrame(selected_rows)

if len(selected_rows) != 0:
    fig = px.bar(selected_rows, "rating", color="type")
    st.plotly_chart(fig)


# streamlit run tut_6.py
# stop: ctrl + c 
