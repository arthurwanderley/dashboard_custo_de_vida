import streamlit as st
import pandas as pd
from utils_continents import show_boxplot, show_barchart, show_scatterplot, mapa_country, graph_continent
from utils import map_display

def continents_page():
    st.title("Continentes")
    st.markdown("Análise de dados por continentes")
    
    df = pd.read_csv('df_cl_ccc_resumido.csv')
    df_resumido = pd.read_csv('df_cl_ccc_resumido_alt.csv')

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

        col1_1, col1_2 = st.columns([3, 1])
        #Filtros
        with col1_1:
            column_names_cv = {
                'CV1_1': 'Mora no Centro da Cidade, utiliza transporte privado',
                'CV1_2': 'Mora no Centro da Cidade, utiliza transporte público',
                'CV2_1': 'Mora Fora do Centro da Cidade, utiliza transporte privado',
                'CV2_2': 'Mora Fora do Centro da Cidade, utiliza transporte público'
            }

            # Criar o selectbox com os nomes amigáveis
            selected_column_cv = st.selectbox(
                'Selecione uma categoria de Custo de Vida',
                options=list(column_names_cv.values()),
                index=0,
            )
            # Encontrar a coluna correspondente no DataFrame
            selected_column_key_cv = [key for key, value in column_names_cv.items() if value == selected_column_cv][0]
       
        ##Filtro Continente
        with col1_2:
            option_continent = st.selectbox(
                "Selecione o Continente",
                df_resumido['Continent'].unique(),
                index=0)
            df_resumido_filtrado = df_resumido[(df_resumido['Continent'] == option_continent)].dropna(subset=['CV1_1', 'CV1_2', 'CV2_1', 'CV2_2'])

        ##Mapa
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            mapa_country(selected_column_key_cv, df_resumido_filtrado)

        with col2_2:
            graph_type = ['Dispersão por Cidade x Salário Médio', 'Composição do Custo do Continente']
            option_graph_type = st.selectbox(
                "Selecione o Tipo do Gráfico",
                graph_type,
                index=0
            )
            graph_continent(option_graph_type, selected_column_key_cv, df_resumido_filtrado, selected_column_cv)

       