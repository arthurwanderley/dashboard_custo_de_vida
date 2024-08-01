import streamlit as st
import pandas as pd
import plotly.express as px

def show_city_barchar(city, country):
    df = pd.read_csv('df_cl_ccc_resumido.csv')

    selected_country_df = df[df['country'] == country]
    
    valor_minimo = selected_country_df['CV1_1'].min()
    valor_maximo = selected_country_df['CV1_1'].max()
    valor_minimo_df = selected_country_df[df['CV1_1'] == valor_minimo]
    valor_maximo_df = selected_country_df[df['CV1_1'] == valor_maximo]
   
    df_filtered_by_city = df[df['city'] == city]

    dataframes = [valor_minimo_df, df_filtered_by_city, valor_maximo_df]

    show_df = pd.concat(dataframes, ignore_index=True)

    fig = px.bar(
        show_df,
        x='city',
        y=['Alimentacao_Basica', 'Transp_Privado', 'Moradia_CentroCidade','Final_de_Semana'],
        title = "Custos de Vida",
        labels = {'continent':'Categorias', 'value':'Valores (USD)', 'variable':'Tipo de despesa'}
    )
    
    with st.container():
        st.plotly_chart(fig)
    
    