import streamlit as st
import base64

def show_image(img_path, backgroundColor='#f2f2f2'):
    st.markdown(f"""
        <div style='display: flex; justify-content: center; background-color: {backgroundColor};
        margin-bottom: 30px;'>
            {_img_to_html(img_path)}
        </div>""",
        unsafe_allow_html=True
    )

def _img_to_bytes(img_path):
    img_bytes = open(img_path, "rb").read()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def _img_to_html(img_path):
    img_html = f"<img src='data:image/png; base64,{_img_to_bytes(img_path)}'; width=600; height=300; class=img-fluid;>"
    return img_html

