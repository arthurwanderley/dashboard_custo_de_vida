import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

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
        height=500
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
    if graph_type == 'Dispersão por Cidade do Continente x Salário Médio':
        plot_scatter_continent(selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio)
    elif graph_type == 'Composição do Custo do Continente':
        plot_bar_chart(selected_column_cv, df_cl_ccc_resumido_filtrado, nome_ficticio)


