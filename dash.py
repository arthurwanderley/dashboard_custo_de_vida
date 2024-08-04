import streamlit as st
from home import home_page
from continents import continents_page
from countries import countries_page
from cities import cities_page
from teste_arthur import main_teste_arthur

st.set_page_config(
    page_title='PAGE_TITLE',
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation([
    st.Page(home_page, title="Home", icon=":material/home:"),
    st.Page(continents_page, title="Continentes", icon="🗺️"),
    st.Page(countries_page, title="Países", icon=":material/map:"),
    st.Page(cities_page, title="Cidades", icon=":material/maps_home_work:"),
    st.Page(main_teste_arthur, title="Teste")
])
pg.run()