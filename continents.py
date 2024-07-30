import streamlit as st
import pandas as pd

def continents_page():
    st.title("Dashboard de Custo de Vida por Continente - CESAR School 24")
    st.markdown("Dashboard com o custo de Vida de diversas cidades do mundo")

    importar = st.button("Importar Dataframe")

    if importar:
        df_cl_ccc_resumido = pd.read_csv('df_cl_ccc_resumido.csv')
        st.dataframe(df_cl_ccc_resumido, hide_index=True)
    else:
        st.write("Sem dados")