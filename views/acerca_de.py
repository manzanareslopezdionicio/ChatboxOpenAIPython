import streamlit as st
from forms.contacto import contact_form

@st.dialog("contacto") #.experimental_dialog("Contacto")
def ver_form_contacto():
    contact_form()
    #name = st.text_input("Nombre:", placeholder="Escribir Nombres")
    #email = st.text_input("Email:", placeholder="nombre@email.com")
    #message = st.text_area("Mensaje:")
    #st.write("---")
    #submit_button = st.button("Enviar", use_container_width=True)

    #if submit_button:
     #   st.success("Mensaje enviado satisfactoriamente...")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("img/dioni.png", width=230)

with  col2:
    st.title("Dionicio Manzanares", anchor=False)
    st.write(
        "Analista de datos senior, que ayuda a las empresas apoyando la toma de decisiones basada en datos. Como Ciencia de Datos."
    )
    if st.button("Contacto"):
        ver_form_contacto()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)