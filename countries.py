import streamlit as st
import pandas as pd
from utils_countries import show_grafico1

def countries_page():
    st.title("Países")
    st.markdown("Análise de dados por países")

    df = pd.read_csv('df_cl_ccc_resumido.csv')

    continents = df['Continent'].unique()

    with st.container():
        continent = st.radio("Selecione um continente", continents, horizontal=True)
        #paises = sorted(df.query('Continent == @continent')['country'].unique())
        #pais = st.multiselect("Selecione um país", paises, placeholder="Selecione")
        #all = st.checkbox("Mostrar todos países")

        show_grafico1(continent)


