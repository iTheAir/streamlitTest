import streamlit as st
import barfi as bi
from barfi import st_barfi, Block

st.title("This is the App title")
x = st.slider('Select a value')
st.write(x, 'squred is', x * x)
st.header("If you like, check below")
st.checkbox('yes')
st.sidebar.title('This is written inside the sidebar')
st.sidebar.button('click')
st.sidebar.radio('Pick your gender', ["male", "female"])

feed = Block(name='Feed')
feed.add_output()

result = Block(name='Result')
result.add_output()

st_barfi(base_blocks=[feed, result])
