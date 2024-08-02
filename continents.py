import streamlit as st
import pandas as pd
from utils_continents import show_boxplot, show_barchart
from utils import show_image

def continents_page():
    st.title("Continentes")
    st.markdown("Análise de dados por continentes")
    show_image('assets/world-map.png')
    
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

        all = st.checkbox("Mostrar todos")

        show_boxplot(option_1, option_2, all)
        show_barchart(option_1, option_2, all)
    