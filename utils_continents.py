import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def show_boxplot(continent_1, continent_2, showAll):
    df = pd.read_csv('df_cl_ccc_resumido.csv')
    df_filtered = df[df['Continent'].isin([continent_1, continent_2])]
    
    # Criando o box plot com plotly.graph_objects
    fig = go.Figure()

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


def show_scatterplot(continent_1, continent_2, show_all=False, lowest_cost=False):
    df = pd.read_csv('df_cl_ccc_resumido.csv')

    if show_all:
        df_with_filters = df
    else:
        df_with_filters = df[df['Continent'].isin([continent_1, continent_2])]
    
    # Definindo símbolos e cores para cada variável
    symbols = ['circle']
    
    column_name = 'CV2_2' if lowest_cost else 'CV1_1'
    columns = [column_name]

    # Criando uma paleta de cores para os continentes
    continent_colors = {
        'Asia': 'purple',
        'Africa': 'green',
        'Europe': 'blue',
        'Americas': 'red',
        'Oceania': 'gray'
    }

    # Criando o scatter plot com plotly.graph_objects
    fig = go.Figure()

    for i, column in enumerate(columns):
        for continent, color in continent_colors.items():
            # Filtrando os dados para o continente atual
            filtered_df = df_with_filters[df_with_filters['Continent'] == continent]

            hover_text = filtered_df['city'] + ', ' + filtered_df['country']

            fig.add_trace(go.Scatter(
                x=filtered_df[column],
                y=filtered_df['Salario_Medio'],
                mode='markers',
                marker=dict(
                    size=6.5,
                    symbol=symbols[i],  # Define o símbolo dos marcadores
                    color=color  # Define a cor baseada no continente
                ),
                text=hover_text,  # Texto a ser exibido no hover
                name=f'{continent}',
                hoverinfo='text'  # Define que o hovertext será exibido
            ))

    # Configurando o layout do gráfico
    fig.update_layout(
        title= "Salário Médio x Residir no fora do centro e usa Transporte público"
            if lowest_cost
            else "Salário Médio x Residir no centro e usa Transporte privado",
        xaxis=dict(
            title="Custo de Vida",
            title_font=dict(size=16),  # Tamanho do título do eixo x
            tickfont=dict(size=14)  # Tamanho dos rótulos do eixo x
        ),
        yaxis=dict(
            title="Salário Médio",
            title_font=dict(size=16),  # Tamanho do título do eixo y
            tickfont=dict(size=14)  # Tamanho dos rótulos do eixo y
        ),
        legend=dict(
            x=0,  # Posição da legenda no eixo x fora do gráfico
            y= -0.6 if show_all else -0.35,  # Posição da legenda no eixo y no topo
            traceorder='normal',
            bgcolor="White",  # Cor de fundo da legenda
            bordercolor="Black",  # Cor da borda da legenda
            borderwidth=1,  # Largura da borda da legenda
            font=dict(
                family="Arial",
                size=12,
                color="black"
            )
        ),
        margin=dict(r=50),
        width=1200,  # Largura do gráfico
        height=550  # Altura do gráfico
    )

    with st.container():
        st.plotly_chart(fig)


def mapa_country(selected_column_key_cv, df_cl_ccc_resumido_filtrado):
    # Calcular o centro do mapa
    center_lat = (df_cl_ccc_resumido_filtrado['Latitude'].min() + df_cl_ccc_resumido_filtrado['Latitude'].max()) / 2
    center_lon = (df_cl_ccc_resumido_filtrado['Longitude'].min() + df_cl_ccc_resumido_filtrado['Longitude'].max()) / 2
    fig = px.scatter_mapbox(
        df_cl_ccc_resumido_filtrado,
        lat="Latitude",
        lon="Longitude",
        hover_name="City",
        size= selected_column_key_cv if selected_column_key_cv in df_cl_ccc_resumido_filtrado.columns else None,  # Usar a coluna 'valor' se ela existir
        height=500,
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_center={"lat": center_lat, "lon": center_lon},
        mapbox_zoom=4  # Ajuste o zoom inicial conforme necessário
    )

    # Ajustar o zoom do mapa para se ajustar aos pontos plotados
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(mapbox={"center": {"lat": center_lat, "lon": center_lon}, "zoom": 2})

    # Mostrar o gráfico na aplicação
    with st.container():
        st.plotly_chart(fig)


def plot_scatter_continent(selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio):
    # Criando o box plot com plotly.graph_objects
    fig = go.Figure()

    hover_text = df_cl_ccc_resumido_filtrado['city']

    #Escala de cor:
    # Calcular as cores com base nas regras fornecidas
    colors = []
    for x, y in zip(df_cl_ccc_resumido_filtrado[selected_column_cv], df_cl_ccc_resumido_filtrado['Salario_Medio']):
        ratio = x / y
        if ratio <= 0.8:
            colors.append('green')
        elif ratio >= 1.2:
            colors.append('red')
        else:
            colors.append('yellow')

    # Adicionar pontos ao gráfico
    fig.add_trace(go.Scatter(
    x=df_cl_ccc_resumido_filtrado[selected_column_cv],
    y=df_cl_ccc_resumido_filtrado['Salario_Medio'],
    mode='markers',
    text=hover_text,  # Texto a ser exibido no hover
    hoverinfo='text',  # Define que o hovertext será exibido
    marker=dict(color=colors),  # Aplicar as cores calculadas
    showlegend=False  # Não mostrar a legenda deste trace
    ))

    #Legenda Fake do Custo de Vida / Salário Médio
    # Adicionar pontos fictícios para a legenda
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='green'),
        legendgroup='green',
        showlegend=True,
        name='CV/Salário Médio <= 0.8'
        ))

    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='yellow'),
        legendgroup='yellow',
        showlegend=True,
        name='0.8 < CV/Salário Médio  < 1.2'
        ))

    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color='red'),
        legendgroup='red',
        showlegend=True,
        name='>= 1.2'
        ))

    # Configurando o layout do gráfico
    fig.update_layout(
        title="Scatter Plot para Variáveis e Salário Médio",
        xaxis=dict(
            title=str(nome_ficticio),
            title_font=dict(size=16),  # Tamanho do título do eixo x
            tickfont=dict(size=14)),  # Tamanho dos rótulos do eixo x
                        
        yaxis=dict(
            title="Salário Médio",
            title_font=dict(size=16),  # Tamanho do título do eixo y
            tickfont=dict(size=14))  # Tamanho dos rótulos do eixo y
        )
    # Mostrar o gráfico na aplicação
    with st.container():
        st.plotly_chart(fig)

def cria_df_cl_ccc_resumido_continente(df_cl_ccc_resumido):
    df_cl_ccc_resumido_continente = df_cl_ccc_resumido[['Continent', 'sub-region', 'Salario_Medio','Alimentacao_Basica',	'Transp_Publico',	'Transp_Privado',	'Moradia_CentroCidade',	'Moradia_ForaCentroCidade',	'Final_de_Semana']]
    df_cl_ccc_resumido_continente = df_cl_ccc_resumido_continente.groupby(['Continent'])[['Salario_Medio', 'Alimentacao_Basica',	'Transp_Publico',	'Transp_Privado',	'Moradia_CentroCidade',	'Moradia_ForaCentroCidade',	'Final_de_Semana']].mean().reset_index()

    #Custo de vida de cada cidade Considerando:
    ##Custo de Vida Mora no Centro da Cidade, utiliza transporte privado e gasta no final de semana --> CV1_1
    df_cl_ccc_resumido_continente['CV1_1'] = df_cl_ccc_resumido_continente['Alimentacao_Basica'] + df_cl_ccc_resumido_continente['Transp_Privado'] + df_cl_ccc_resumido_continente['Moradia_CentroCidade'] + df_cl_ccc_resumido_continente['Final_de_Semana']

    ##Custo de Vida Mora no Centro da Cidade, utiliza transporte publico e gasta no final de semana --> CV1_2
    df_cl_ccc_resumido_continente['CV1_2'] = df_cl_ccc_resumido_continente['Alimentacao_Basica'] + df_cl_ccc_resumido_continente['Transp_Publico'] + df_cl_ccc_resumido_continente['Moradia_CentroCidade'] + df_cl_ccc_resumido_continente['Final_de_Semana']

    ##Custo de Vida Mora Fora do Centro da Cidade, utiliza transporte privado e gasta no final de semana --> CV2_1
    df_cl_ccc_resumido_continente['CV2_1'] = df_cl_ccc_resumido_continente['Alimentacao_Basica'] + df_cl_ccc_resumido_continente['Transp_Privado'] + df_cl_ccc_resumido_continente['Moradia_ForaCentroCidade'] + df_cl_ccc_resumido_continente['Final_de_Semana']

    ##Custo de Vida Mora Fora Centro da Cidade, utiliza transporte publico e gasta no final de semana --> CV2_2
    df_cl_ccc_resumido_continente['CV2_2'] = df_cl_ccc_resumido_continente['Alimentacao_Basica'] + df_cl_ccc_resumido_continente['Transp_Publico'] + df_cl_ccc_resumido_continente['Moradia_ForaCentroCidade'] + df_cl_ccc_resumido_continente['Final_de_Semana']
    return df_cl_ccc_resumido_continente

def plot_bar_chart(selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio):
    df_cl_ccc_resumido_continente_filtrado = cria_df_cl_ccc_resumido_continente(df_cl_ccc_resumido_filtrado)
    if selected_column_cv == 'CV1_1':
        colunas_plot = ['Alimentacao_Basica', 'Transp_Privado', 'Moradia_CentroCidade', 'Final_de_Semana']
    elif selected_column_cv == 'CV1_2':
        colunas_plot = ['Alimentacao_Basica', 'Transp_Publico', 'Moradia_CentroCidade', 'Final_de_Semana']
    elif selected_column_cv == 'CV2_1':
        colunas_plot = ['Alimentacao_Basica', 'Transp_Privado', 'Moradia_ForaCentroCidade', 'Final_de_Semana']
    elif selected_column_cv == 'CV2_2':
        colunas_plot = ['Alimentacao_Basica', 'Transp_Publico', 'Moradia_ForaCentroCidade', 'Final_de_Semana']
    
    fig = px.bar(df_cl_ccc_resumido_continente_filtrado, x='Continent', y=colunas_plot,
             title = 'Distribuição dos Custos de Vida por Continente',
             labels = {'continent':'Categorias', 'value':'Valores (USD)', 'variable':'Tipo de despesa'}
             )
    # Mostrar o gráfico na aplicação
    with st.container():
        st.plotly_chart(fig)
    

def graph_continent(graph_type, selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio):
    if graph_type == 'Dispersão por Cidade x Salário Médio':
        plot_scatter_continent(selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio)
    elif graph_type == 'Composição do Custo do Continente':
        plot_bar_chart(selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio)



    