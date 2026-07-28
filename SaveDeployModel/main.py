from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load('iris_model.pkl')

@app.get('/')
def root():
  return{'message':"ML model is running"}

@app.post('/predict')
def predict(sepal_length:float,sepal_width:float,petal_length:float,petal_width:float):
  data = pd.DataFrame([[sepal_length,sepal_width,petal_length,petal_width]],
                      columns=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)'])
  prediction = model.predict(data)[0]
  return {'prediction_class':int(prediction)}

