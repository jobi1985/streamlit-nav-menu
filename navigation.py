import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    
if selected =="Home":
    st.title(f"You have selected {selected}")
if selected =="Settings":
    st.title(f"You have selected {selected}")
