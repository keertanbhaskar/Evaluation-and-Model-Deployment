import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('Titanic-Dataset.csv')
print(data.shape) 

le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])
X = data[['Age','Pclass','Fare','Sex']]
y = data['Survived']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True)

model = RandomForestClassifier()
scores = cross_val_score(model,X,y,cv=5)
print('cross-val score:',scores)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)


# classification report
print(classification_report(y_test,y_pred))

test_data = [[25,1,72.5,1]]
prediction = model.predict(test_data)
print("prediction:",prediction) # 0 => not survived, 1 =>survived


print("Accu score:",accuracy_score(y_test,y_pred))