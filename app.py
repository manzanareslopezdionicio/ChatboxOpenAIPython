import streamlit as st

#Variables de secion de mensajes
st.title("🤖 Asistente Virtual - IA")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]): # Definir el rol del mensaje
        st.markdown(message["content"]) # Mostrar el mensaje

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿Comó puedo ayudarte?")

    st.session_state.messages.append({"role": "assistant",  "content": "Hola, ¿Comó puedo ayudarte?"})
    st.session_state.first_message = False

if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role":"assistant", "content": prompt})

   # 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