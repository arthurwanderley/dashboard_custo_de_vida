import streamlit as st
import pandas as pd
from utils.utils_cities import show_city_barchar_high_cost,show_city_barchar_low_cost, show_mapbox
from utils.utils import show_country_flag

def cities_page():
    st.title("Cidades")
    st.markdown("Análise de dados por cidades")

    df = pd.read_csv('df_cl_ccc_resumido.csv')
  
    continents = df['Continent'].unique()
    tupla_continents = tuple(continents)

    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        index_americas = tupla_continents.index("Americas")

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
        tupla_cities = tuple(cities_list)
    
        with col3:
            option_3 = st.selectbox(
            "Selecione uma cidade",
            tupla_cities,
            )
            
        with col4:
            show_country_flag(option_2)

        show_mapbox(option_3)
        show_lower_higher_cities_costs = st.toggle("Mostrar cidades com menor e maior custo", value=True)
        show_city_barchar_high_cost(option_3, option_2, show_lower_higher_cities_costs)
        show_city_barchar_low_cost(option_3, option_2, show_lower_higher_cities_costs)