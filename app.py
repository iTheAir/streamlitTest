import streamlit as st

st.title("This is the App title")
x = st.slider('Select a value')
st.write(x, 'squred is', x * x)
st.header("If you like, check below")
st.checkbox('yes')
