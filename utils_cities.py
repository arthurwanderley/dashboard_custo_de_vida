import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_city_coordenates

def show_mapbox(city_selected):
    coordenates = get_city_coordenates()
    df = pd.DataFrame(coordenates.items(), columns=['city', 'coordinates'])
    df[['lat', 'lon']] = pd.DataFrame(df['coordinates'].tolist(), index=df.index)
    df = df.drop(columns=['coordinates'])
    
    # Obter coordenadas da cidade selecionada
    selected_coordinates = df[df['city'] == city_selected][['lat', 'lon']].values[0]
    
    fig = px.scatter_mapbox(
        df,
        lat="lat",
        lon="lon",
        hover_name="city",
        color_discrete_sequence=["fuchsia"], zoom=3,
        height=280
    )

    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_center={"lat": selected_coordinates[0], "lon": selected_coordinates[1]},
        mapbox_zoom=7,
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
        ])
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    
    with st.container():
        st.plotly_chart(fig)


def show_city_barchar_high_cost(city, country, show_min_max_cost):
    df = pd.read_csv('df_cl_ccc_resumido.csv')

    selected_country_df = df[df['country'] == country]
    df_filtered_by_city = df[df['city'] == city]

    if show_min_max_cost:
        valor_minimo = selected_country_df['CV1_1'].min()
        valor_maximo = selected_country_df['CV1_1'].max()
        valor_minimo_df = selected_country_df[df['CV1_1'] == valor_minimo]
        valor_maximo_df = selected_country_df[df['CV1_1'] == valor_maximo]
   
        dataframes = [valor_minimo_df, df_filtered_by_city, valor_maximo_df]
        show_df = pd.concat(dataframes, ignore_index=True)
    else:
        show_df = df_filtered_by_city
    
    fig = px.bar(
        show_df,
        x='city',
        y=['Alimentacao_Basica', 'Transp_Privado', 'Moradia_CentroCidade','Final_de_Semana'],
        title = "Custos de Vida - Mora no centro e usa transporte privado",
        labels = {'continent':'Categorias', 'value':'Valores (USD)', 'variable':'Tipo de despesa'}
    )

    with st.container():
        st.plotly_chart(fig)


def show_city_barchar_low_cost(city, country, show_min_max_cost):
    df = pd.read_csv('df_cl_ccc_resumido.csv')

    selected_country_df = df[df['country'] == country]
    df_filtered_by_city = df[df['city'] == city]

    if show_min_max_cost:
        valor_minimo = selected_country_df['CV2_2'].min()
        valor_maximo = selected_country_df['CV2_2'].max()
        valor_minimo_df = selected_country_df[df['CV2_2'] == valor_minimo]
        valor_maximo_df = selected_country_df[df['CV2_2'] == valor_maximo]
   
        dataframes = [valor_minimo_df, df_filtered_by_city, valor_maximo_df]
        show_df = pd.concat(dataframes, ignore_index=True)
    else:
        show_df = df_filtered_by_city

    fig = px.bar(
        show_df,
        x='city',
        y=['Alimentacao_Basica', 'Transp_Publico', 'Moradia_ForaCentroCidade','Final_de_Semana'],
        title = "Custos de Vida - Mora fora do centro e usa transporte público",
        labels = {'continent':'Categorias', 'value':'Valores (USD)', 'variable':'Tipo de despesa'}
    )

    with st.container():
        st.plotly_chart(fig)

   
    
    