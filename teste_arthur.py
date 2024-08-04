import pandas as pd
import streamlit as st
import plotly.express as px
from utils_teste_arthur import mapa_country, graph_continent

df_cl_ccc_resumido = pd.read_csv('df_cl_ccc_resumido_alt.csv')

def main_teste_arthur():
    ## 1. Filtro e Continente
    # Dicionário com os nomes das colunas e os nomes amigáveis

    col1_1, col1_2 = st.columns([3, 1])
    #Filtros
    ##Filtro CV
    with col1_1:
        column_names_cv = {
            'CV1_1': 'Mora no Centro da Cidade, utiliza transporte privado e gasta no final de semana',
            'CV1_2': 'Mora no Centro da Cidade, utiliza transporte público e gasta no final de semana',
            'CV2_1': 'Mora Fora do Centro da Cidade, utiliza transporte privado e gasta no final de semana',
            'CV2_2': 'Mora Fora do Centro da Cidade, utiliza transporte público e gasta no final de semana'}
        # Criar o selectbox com os nomes amigáveis
        selected_column_cv = st.selectbox(
            'Selecione um Custo de Vida para Filtrar',
            options=list(column_names_cv.values()),
            index=0,
        )
        # Encontrar a coluna correspondente no DataFrame
        selected_column_key_cv = [key for key, value in column_names_cv.items() if value == selected_column_cv][0]
    ##Filtro Continente
    with col1_2:
        option_continent = st.selectbox(
            "Selecione o Continente",
            df_cl_ccc_resumido['Continent'].unique(),
            index=0)
        df_cl_ccc_resumido_filtrado = df_cl_ccc_resumido[(df_cl_ccc_resumido['Continent'] == option_continent)].dropna(subset=['CV1_1', 'CV1_2', 'CV2_1', 'CV2_2'])

    ## 2.1. Mapa
    col2_1, col2_2 = st.columns([3, 2])
    with col2_1:
        mapa_country(selected_column_key_cv, df_cl_ccc_resumido_filtrado)

    with col2_2:
        graph_type = ['Dispersão por Cidade do Continente x Salário Médio', 'Composição do Custo do Continente']
        option_graph_type = st.selectbox(
            "Selecione o Tipo do Gráfico",
            graph_type,
            index=0)
        graph_continent(option_graph_type, selected_column_key_cv, df_cl_ccc_resumido_filtrado, selected_column_cv)