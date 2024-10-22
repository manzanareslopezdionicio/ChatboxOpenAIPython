import streamlit as st

home = st.Page  (
    page="views/home.py",
    title="Inicio",
    icon=":material/home:",
    default=True,
)

acerca_de_page = st.Page(
    page="views/acerca_de.py",
    title="Acerca de",
    icon=":material/account_circle:",
)
project_1_page = st.Page(
    page="views/ventas.py",
    title="ventas",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

pg = st.navigation(
    {
        "Información:": [home, acerca_de_page],
        "Projectos:": [project_1_page, project_2_page],
    }
)



# --- SHARED ON ALL PAGES ---
st.logo("img/chatbot.png")
st.sidebar.markdown("Elaborado con ❤️ por [Streamlit](https://streamlit.io/gallery)")


# --- RUN NAVIGATION ---
pg.run()