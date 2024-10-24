import streamlit as st

#configuracion

#st.set_page_config(layout='wide')

with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA :wave:")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tecnologia y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
    )
st.write("[Saber más >](https://streamlit.io/)")

# Sobre nosotros
with st.container():
    st.write("---")
    I_columna, R_columna = st.columns((2))
    with I_columna:
        st.header("Sobre nosotros 🔍")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
        )
        st.write("[Más sobre nosotros >](https://streamlit.io/)")
    with R_columna:
        st.empty()
    
    #Servicios
    with st.container():
        st.write("---")
        st.header("Servicios")
        #st.write("##")
        imagen_columna, texto_columna = st.columns((1,2))
        with imagen_columna:
            st.image("img/chatbot.png")
        
        with texto_columna:
            st.subheader("Diseño de aplicaciones")
            st.write(
                """
                Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
                """
            )
            st.write("[Ver servicios > ](https://streamlit.io/)")
    
    with st.container():
        st.write("---")
        #st.write("##")
        imagen_columna, texto_columna = st.columns((1,2))
        with imagen_columna:
            st.image("img/chatbot.png")
        
        with texto_columna:
            st.subheader("Automatización de procesos")
            st.write(
                """
                Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras tareas más productivas.
                """
            )
            st.write("[Ver servicios > ](https://streamlit.io/)")

    with st.container():
        st.write("---")
        #st.write("##")
        imagen_columna, texto_columna = st.columns((1,2))
        with imagen_columna:
            st.image("img/chatbot.png")
        
        with texto_columna:
            st.subheader("Visualización de datos")
            st.write(
                """
                Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una aplicación en la que puedas tener toda la información de interes de tu empresa.
                """
            )
            st.write("[Ver servicios > ](https://streamlit.io/)")

        