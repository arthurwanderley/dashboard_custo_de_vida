import streamlit as st
import pandas as pd
import plotly.express as px

def show_grafico1(paises, continent, all):
    df = pd.read_csv('df_cl_ccc_resumido.csv')

    if all:
        df_filtered = df.query('Continent == @continent').groupby('country')[['Alimentacao_Basica', 'Transp_Privado', 'Moradia_CentroCidade', 'Final_de_Semana']].mean().reset_index()
    else:
        df_filtered = df.query('country == @paises').groupby('country')[['Alimentacao_Basica', 'Transp_Privado', 'Moradia_CentroCidade', 'Final_de_Semana']].mean().reset_index()
    
    df_filtered.rename(columns = {'Alimentacao_Basica':'Alimentacao basica', 'Transp_Privado':'Transp privado', 
                                 'Moradia_CentroCidade':'Moradia - centro da cidade', 'Final_de_Semana':'Final de semana'}, inplace = True)

    fig = px.bar(df_filtered, x='country', y=['Alimentacao basica', 'Transp privado', 'Moradia - centro da cidade', 'Final de semana'],
            title = 'Distribuição dos Custos de Vida',
            labels = {'country':'Países', 'value':'Valores (USD)', 'variable':'Tipo de despesa'}
        )
    
    with st.container():
        st.plotly_chart(fig)
