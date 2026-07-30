import streamlit as st
import joblib
import pandas as pd
from PIL import Image

model = joblib.load('iris_model.pkl')

st.title('Iris Flower Classification')

# sepal_length = st.slider('Sepal Length (cm)',4.0,8.0)
# sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0)
# petal_length = st.slider("Petal Length (cm)", 1.0, 7.0)
# petal_width = st.slider("Petal Width (cm)", 0.1, 2.5)

sepal_length = st.number_input('Sepal Length (cm) 4.0,8.0')
sepal_width = st.number_input('Sepal Width (cm)  2.0, 5.0')
petal_length = st.number_input("Petal Length (cm) 1.0, 7.0")
petal_width = st.number_input("Petal Width (cm) 0.1, 2.5")

features = [[sepal_length, sepal_width, petal_length, petal_width]]

flower_names = {
    0:'setosa',
    1:"versicolor",
    2:'virginica'
}

flowers_img = {
    'setosa':"images/setosa.png",
    "versicolor":"images/vercicolor.png",
    "virginica" : "images/virginica.png"
}
if st.button("Predict"):
    prediction = model.predict(features)[0]
    flower = flower_names[prediction]
    st.success(f"Predicted Iris Class: {flower.title()}")

    image = Image.open(flowers_img[flower])
    st.image(image,caption=flower.title(),width=350,)

