import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def show_boxplot(continent_1, continent_2, showAll):
    df = pd.read_csv('df_cl_ccc_resumido.csv')
    df_filtered = df[df['Continent'].isin([continent_1, continent_2])]
    
    # Criando o box plot com plotly.graph_objects
    fig = go.Figure()

    categorias = ['CV1_1', 'CV1_2', 'CV2_1', 'CV2_2']
    # Dicionário de mapeamento de nomes de categorias
    category_names = {
        'CV1_1': 'CV Moradia no Centro da Cidade, utiliza\n transporte privado e gasta no final de semana',
        'CV1_2': 'CV Moradia no Centro da Cidade, utiliza\n transporte público e gasta no final de semana',
        'CV2_1': 'CV Moradia fora do Centro da Cidade, utiliza\n transporte privado e gasta no final de semana',
        'CV2_2': 'CV Moradia fora do Centro da Cidade, utiliza\n transporte público e gasta no final de semana'
    }

    for category, custom_name in category_names.items():
        fig.add_trace(go.Box(
                y=df[category] if showAll else df_filtered[category],
                x=df['Continent'] if showAll else df_filtered['Continent'],
                #boxpoints=False, # no data points
                name=custom_name
            ))

    # Configurando o layout do gráfico
    fig.update_layout(
        title="Custos de Vida por Continente",
        height=600,
        title_font=dict(size=20),  # Tamanho do título
        xaxis=dict(
            title="Continente",
            title_font=dict(size=18),  # Tamanho do título do eixo x
            tickfont=dict(size=18)  # Tamanho dos rótulos do eixo x
        ),
        yaxis=dict(
            title="$USD",
            title_font=dict(size=18),  # Tamanho do título do eixo y
            tickfont=dict(size=14)  # Tamanho dos rótulos do eixo y
        ),
        boxmode='group',  # Agrupa os boxes por continente
        #Personalização da Legenda
        legend=dict(
            #title="Categorias",
            x=0,  # Posição da legenda no eixo x
            y= -0.3,  # Posição da legenda no eixo y
            bgcolor="Lavender",  # Cor de fundo da legenda
            bordercolor="Black",  # Cor da borda da legenda
            borderwidth=1,  # Largura da borda da legenda
            orientation="h",  # Orientação horizontal
            font=dict(
                #family="Arial",
                size=16,
                color="black"
            )
        )
    )

    with st.container():
        st.plotly_chart(fig)


def show_barchart(continent_1, continent_2, showAll):
    # Criando o box plot com plotly.graph_objects
    fig = go.Figure()

    df = pd.read_csv('df_cl_ccc_resumido.csv')
    df_filtered = df[df['Continent'].isin([continent_1, continent_2])]

    categorias = ['Salario_Medio', 'CV1_1', 'CV1_2', 'CV2_1', 'CV2_2']
    # Dicionário de mapeamento de nomes de categorias
    category_names = {
        'Salario_Medio': 'Salário Médio',
        'CV1_1': 'CV Moradia no Centro da Cidade, utiliza transporte privado e gasta no final de semana',
        'CV1_2': 'CV Moradia no Centro da Cidade, utiliza transporte público e gasta no final de semana',
        'CV2_1': 'CV Moradia fora do Centro da Cidade, utiliza transporte privado e gasta no final de semana',
        'CV2_2': 'CV Moradia fora do Centro da Cidade, utiliza transporte público e gasta no final de semana'
    }

    for category, custom_name in category_names.items():
        fig.add_trace(go.Bar(
                y=df[category] if showAll else df_filtered[category],
                x=df['Continent'] if showAll else df_filtered['Continent'],
                name=custom_name
            ))

    # Configurando o layout do gráfico
    fig.update_layout(
        title="Salário x Custo de Vida",
        height=600,
        title_font=dict(size=20),
        xaxis=dict(
            title="Continente",
            title_font=dict(size=18),  # Tamanho do título do eixo x
            tickfont=dict(size=16)  # Tamanho dos rótulos do eixo x
        ),
        yaxis=dict(
            title="$USD",
            title_font=dict(size=18),  # Tamanho do título do eixo y
            tickfont=dict(size=16)  # Tamanho dos rótulos do eixo y
        ),
        barmode='group',
        legend=dict(
            x=0,  # Posição da legenda no eixo x fora do gráfico
            y=-0.8,  # Posição da legenda no eixo y no topo
            traceorder='normal',
            bgcolor="White",  # Cor de fundo da legenda
            bordercolor="Black",  # Cor da borda da legenda
            borderwidth=1,  # Largura da borda da legenda
            font=dict(
                family="Arial",
                size=16,
                color="black"
            )
        )
    )

    with st.container():
        st.plotly_chart(fig)
    