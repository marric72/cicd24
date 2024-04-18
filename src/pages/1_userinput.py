import streamlit as st
import pandas as pd
import numpy as np
from requests import get


# Write text to the screen with HTML markup
title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CS399 Streamlit Test</p>'
st.markdown(title, unsafe_allow_html=True)
st.image("panda.png", caption='Hello')
title = '<p style="font-family:Courier; color:White; font-size: 20px;">Exchange Rates </p>'
st.markdown(title, unsafe_allow_html=True)

# write user input to screen
n = st.text_input("Enter name")
if len(n) > 0:
    title = f'<p style="font-family:Courier; color:Blue; font-size: 20px;">Welcome {
        n}</p>'
    st.markdown(title, unsafe_allow_html=True)
