import streamlit as st
import pandas as pd
import numpy as np

st.logo('https://upload.wikimedia.org/wikipedia/commons/2/2e/Syarah_Logo.png')

st.set_page_config(layout='centered')
st.markdown("<h1 style='text-align: right; '>هل أريد شراء سيارة مستعملة؟</h1>", unsafe_allow_html=True)

Welcome_text = '''
<div style="text-align: right"> 

</div>
'''
st.image("Everyday LA.gif")


another = '<div style="text-align: right"> هلا! </div>'
st.html(Welcome_text)
st.html(another)