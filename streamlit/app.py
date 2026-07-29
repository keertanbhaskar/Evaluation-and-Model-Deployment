import streamlit as st
import joblib
import pandas as pd

model = joblib.load('iris_model.pkl')

st.title('Iris Flower Classification')

sepal_length = st.slider('Sepal Length (cm)',4.0,8.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5)

features = [[sepal_length, sepal_width, petal_length, petal_width]]

if st.button("Predict"):
    prediction = model.predict(features)[0]
    st.success(f"Predicted Iris Class: {prediction}")