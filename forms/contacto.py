import re

import streamlit as st
#import requests  # pip install requests

#WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Nombres y Apellidos.")
        email = st.text_input("Correo electrónico:")
        message = st.text_area("Su Mensaje:")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        
        if not name:
            st.error("Por favor escriba su nombre.", icon="🧑")
            st.stop()

        if not email:
            st.error("Por favor escriba su dirección de correo electrónico.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Por favor su dirección de correo electrónico no es correcto.", icon="📧")
            st.stop()

        if not message:
            st.error("Por favor escriba un mensaje.", icon="💬")
            st.stop()
        
        if submit_button: 
            st.success("Se envio satisfactoriamente.")
            st.rerun()
       