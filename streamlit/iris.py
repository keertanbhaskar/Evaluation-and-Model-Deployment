from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd

data = load_iris(as_frame=True)
X = data.data
y = data.target

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,'iris_model.pkl')