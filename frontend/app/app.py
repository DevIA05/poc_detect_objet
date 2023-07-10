import requests
import streamlit as st
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SightAI", page_icon=":skull:", layout="centered")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Bonjour, bienvenue chez SightAI :wave:")
    st.title("")
    st.write("")