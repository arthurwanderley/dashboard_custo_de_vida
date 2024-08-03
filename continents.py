import streamlit as st
import pandas as pd
from utils_continents import show_boxplot, show_barchart, show_scatterplot
from utils import map_display

def continents_page():
    st.title("Continentes")
    st.markdown("Análise de dados por continentes")
    
    df = pd.read_csv('df_cl_ccc_resumido.csv')
    continents = df['Continent'].unique()
    tupla_continents = tuple(continents)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            option_1 = st.selectbox(
            "Selecione um continente",
            tuple(tupla_continents),
            )
        with col2:
            option_2 = st.selectbox(
            "Selecione um continente",
            tuple(item for item in tupla_continents if item != option_1),
            )

        show_all = st.checkbox("Mostrar todos")

        map_display(option_1, option_2, show_all)
        show_boxplot(option_1, option_2, show_all)
        show_barchart(option_1, option_2, show_all)
        
        col3, col4 = st.columns(2)
        
        with col3:
            show_scatterplot(option_1, option_2, show_all=show_all, lowest_cost=True)
        with col4:
            show_scatterplot(option_1, option_2, show_all=show_all)