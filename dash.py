import streamlit as st
from view.home import home_page
from view.continents import continents_page
from view.countries import countries_page
from view.cities import cities_page

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
)

pg = st.navigation([
    st.Page(home_page, title="Home", icon=":material/home:"),
    st.Page(continents_page, title="Continentes", icon="🗺️"),
    st.Page(countries_page, title="Países", icon=":material/map:"),
    st.Page(cities_page, title="Cidades", icon=":material/maps_home_work:"),
])
pg.run()