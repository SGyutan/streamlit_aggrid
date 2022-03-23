# tut_4.py
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# add
from st_aggrid.shared import JsCode

st.set_page_config(page_title="Netflix Shows", layout="wide") 
st.title("Netlix shows analysis")

shows = pd.read_csv("netflix_titles.csv")
gb = GridOptionsBuilder.from_dataframe(shows)

# ---

cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('United States')) {
        return {
            'color': 'white',
            'backgroundColor': 'darkred'
        }
    } else {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    }
};
"""
)

gb.configure_column("country", cellStyle=cellsytle_jscode)

gridOptions = gb.build()

data = AgGrid(
    shows,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    allow_unsafe_jscode=True
)


# streamlit run tut_4.py
# stop: ctrl + c 