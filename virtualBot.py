import streamlit as st
import time
from groq import Groq
from typing import Generator
from PIL import Image

#st.title("Estamos la etapa de prueba")

img = Image.open("./img/chatbot.png")

st.set_page_config(page_title='Mi APP IA', page_icon=img,
                   initial_sidebar_state="collapsed")

#titulo CharBot
st.markdown("### Estamos en la etapa de prueba \n # Bienvenidos ")

st.title("🤖 Asistente Virtual - IA")

#Declaracion del cliente Groq
client = Groq (
    api_key=st.secrets["ngroqAPIKey"] #Carga el API key del .streamlit/secrets.toml
)

#Lista de modelos para elegir
modelos = ['llama3-8b-8192', 'llama3-70b-8192', 'maxtral-8x7b-32768']

def generate_chat_responses(char_completion) -> Generator[str, None, None]:
    """ Generated Chat Responses
        Genera respuestas de Chat a partir de la información de completado de chat, mostrando caracter por caracter.
        Args: chat_completion (str): La informacion de completado de chat.
        Yields: str: Cada respuesta generada.
    """
    for chunk in char_completion:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

#Inicializando el historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Muestra mensajes de chat desde la historia en la aplicacion cada vez que la aplicacion se ejecuta
with st.container():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): # Definir el rol del mensaje
            st.markdown(message["content"]) # Mostrar el mensaje

# Mostrar la lista de modelos en la sidebar
parModelo = st.sidebar.selectbox ('Modelos:', options=modelos, index=0)

# Mostrar el campo para el prompt del usuario
prompt = st.chat_input("Hola, ¿Comó puedo ayudarte?")

if prompt:
    # Mostrar el mensaje de usuario en el contenedor de mensajes de chat
    st.chat_message("user").markdown(prompt)

    # Agregar mensaje de usuario al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    try:
        chat_completion = client.chat.completions.create(
            model=parModelo,
            messages=[
                {
                    "role":  m["role"],
                    "content": m["content"]
                }
                for m in st.session_state.messages
            ], # Entrega el historial de los mensajes para que el modelo tenga algo en memoria
            stream=True
        )
        # Mostrar respuesta del asistente en el contenedor de mensajes de char
        with st.chat_message("assistant"):
            chat_responses_generator = generate_chat_responses(chat_completion)

            # Usar st.write_stream para simular escritura
            full_response = st.write_stream(chat_responses_generator)

            # Agregar respuesta de asistente al historial de chat
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    except Exception as e: # Informa si hay error
        st.error(e)
