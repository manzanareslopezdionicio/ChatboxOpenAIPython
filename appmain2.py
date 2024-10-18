import streamlit as st
from streamlit_option_menu import option_menu

# menu vertical
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected

# Menu horizontal
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['horse', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2
