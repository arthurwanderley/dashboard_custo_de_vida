import streamlit as st
import pandas as pd
from utils_cities import show_city_barchar_high_cost,show_city_barchar_low_cost, show_mapbox

def cities_page():
    st.title("Cidades")
    st.markdown("Análise de dados por cidades")

    df = pd.read_csv('df_cl_ccc_resumido.csv')

    continents = df['Continent'].unique()
    tupla_continents = tuple(continents)

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            option_1 = st.selectbox(
            "Selecione um continente",
            tuple(tupla_continents),
            )

        selected_continent_df = df[df['Continent'] == option_1]
        countries_list = selected_continent_df['country'].unique()
       
        with col2:
            option_2 = st.selectbox(
            "Selecione um país",
            tuple(countries_list),
            )

        selected_country_df = df[df['country'] == option_2]
        cities_list = selected_country_df['city'].unique()

        with col3:
            option_3 = st.selectbox(
            "Selecione uma cidade",
            tuple(cities_list),
            )

        show_mapbox(option_3)
        show_city_barchar_high_cost(option_3, option_2)
        show_city_barchar_low_cost(option_3, option_2)