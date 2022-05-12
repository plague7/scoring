# Librairies
import streamlit as st
import pandas as pd
import numpy as np
import gc
import pickle as pkl
import plotly_express as px
from PIL import Image 

# Header
#t1, t2 = st.columns((0.01,1)) 
#t1.image('images/image.png', width = 120)
#t2.title("Home Credit Default Risk 💳")

img = Image.open("image.png") 
st.image(img, width=120) 

st.write("""
# Home Credit Default Risk 📈
""")

# Import Dataset test
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.drop('Unnamed: 0', inplace=True, axis=1)
    st.write(df.head())
    st.selectbox('Choose ID', df)

    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['EXT_SOURCE_1', 'EXT_SOURCE_2','EXT_SOURCE_3'])

    st.line_chart(df)

