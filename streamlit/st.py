import streamlit as st
st.title('Iris Prediction')

st.header('keertana')
name = st.text_input("Enter name")

if st.button('click'):
  st.write("Hello",name)