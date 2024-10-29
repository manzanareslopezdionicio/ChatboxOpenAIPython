import json
import requests
import streamlit as st 
from streamlit_lottie import st_lottie

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)
    
path = get("./lf.json")
st_lottie(path)
