import streamlit as st

@st.dialog("contacto") #.experimental_dialog("Contacto")
def form_contacto():
    st.text_input("Email", placeholder="nombre@email.com")
    st.text_input("Nombre", placeholder="Escribir Nombres")
    st.text_input("Apellidos", placeholder="Escribir Apellidos")
    password = st.text_input("Password", placeholder="password")
    st.write("---")
    st.button("Enviar", use_container_width=True)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("img/dioni.png", width=230)

with  col2:
    st.title("Dionicio Manzanares", anchor=False)
    st.write(
        "Analista de datos senior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. Como Ciencia de Datos."
    )
    if st.button("Contacto"):
        form_contacto()