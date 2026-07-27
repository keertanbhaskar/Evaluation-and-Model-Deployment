from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import classification_report,accuracy_score
from sklearn.preprocessing import LabelEncoder


import pandas as pd

data = pd.read_csv('Titanic-Dataset.csv')
print(data.isnull().sum()) #Age 177 missing

data['Age'] = data['Age'].fillna(data['Age'].mean())

le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
X = data[['Age','Pclass','Fare','Sex']]
y = data['Survived']

# print(X) 1=>male 0 => female
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True)


model = GaussianNB()
scores = cross_val_score(model,X,y,cv=5)
print("Cross-val:",scores)
model.fit(X_train,y_train)


y_pred = model.predict(X_test)
print(classification_report(y_test,y_pred))
print('Acc Score:',accuracy_score(y_test,y_pred))


prediction = [[22,1,75.5,]]