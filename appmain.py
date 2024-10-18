import streamlit as st



#Textos en pantalla
st.title("Curso de Streamlit")
st.header("Esto es un encabezado")
st.subheader("Esto es un sub encabezado")
st.text("Hola esto es un texto")
nombre  = "Dionicio"
st.text(f"Hola {nombre}, esto es un texto de prueba")
st.markdown("# Este es un markdown h1 \n ### Este es un h2 \n ### Este es un h3")
st.write("Este es una mensaje con WRITE")
st.write("## Este es un texto de markdown")
st.write(5+3)

#Mensajes de alerta
st.success("Exito")
st.warning("Esto es una advertencia")
st.info("Esto es informacion")
st.error("Esto es un error")
st.exception("Esto es una excepcion")

#input
nombres = st.text_input("Ingresa tu nombre")
st.write(nombres)

mensaje = st.text_area("Ingresa tu nombre")
st.write(mensaje)

numero = st.number_input("Ingresar un numero", 1, 25)
st.write(numero)

cita = st.date_input("Selecciona una fecha")
st.write(cita)

hora = st.time_input("Selecciona la hora")
st.write(hora)

color = st.color_picker("Selecciona un color")
st.write(color)

st.button("Enviar", type="primary")
st.button("Say hello", icon=":material/mood:", use_container_width=True)
st.link_button("Go to gallery", "https://streamlit.io/gallery", type="primary")

#Abrir una Archivo
st.image("img/chatbot.png")
st.audio("musica/Elton John - Sacrifice.mp3", loop=True)
st.video("video/Video_Streamlit.mp4")

st.subheader("Archivo de imagen")
st.image("img/chatbot.png", width=300, caption="Simple Imagen")