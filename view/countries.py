import streamlit as st
import pandas as pd
from utils.utils_countries import show_grafico1

def countries_page():
    st.title("Países")
    st.markdown("Análise de dados por países")

    df = pd.read_csv('df_cl_ccc_resumido.csv')

    continents = df['Continent'].unique()

    with st.container():
        continent = st.radio("Selecione um continente", continents, horizontal=True)
        all = st.checkbox("Mostrar todos países", value=True)
        paises = sorted(df.query('Continent == @continent')['country'].unique())
        paises_selecionados = st.multiselect("Selecione um ou mais países", paises, placeholder="Selecione", disabled=all, default=paises[0])
        
        show_grafico1(paises_selecionados, continent, all)