import streamlit as st

x = st.slider('Select a value')
st.write(x, 'squred is', x * x)
