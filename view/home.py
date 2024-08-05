import streamlit as st
from utils.utils import resize_image

def home_page():
    st.title("Dash World Cost")
    st.markdown("Para explorar o custo de vida por continentes, países e cidades!")

    with st.container():
       st.markdown(f"""
            <p> Analise as diferenças de valores em se morar no centro, fora do centro,<br> 
                utilizando transporte público ou privado e muito mais. <br>
                Moeda referencial: <strong>Dólar Americano(US$)</strong>
            </p>""",
            unsafe_allow_html=True
        )
    
    paris_img = resize_image('assets/paris.jpg', 260)
    tokyo_img = resize_image('assets/tokyo.jpg', 260)
    olinda_img = resize_image('assets/olinda.jpg', 260)
    newyork_img = resize_image('assets/newyork.jpg', 260)

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image(paris_img, caption='Paris, França')
            
        with col2:
            st.image(tokyo_img, caption='Tokyo, Japão')

        with col3:
            st.image(olinda_img, caption='Olinda, Brasil')

        with col4:
            st.image(newyork_img, caption='Nova York, EUA')