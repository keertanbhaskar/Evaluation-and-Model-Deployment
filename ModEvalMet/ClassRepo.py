from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,ConfusionMatrixDisplay,accuracy_score
import matplotlib.pyplot as plt

# Sample data
messages = [
    "Win cash now",
    "Free vacation offer",
    "Claim your reward",
    "Congratulations you won",
    "Exclusive discount",
    "Get free money",
    "Lottery winner",
    "Click here to claim",
    "Your OTP is 4567",
    "Let's meet tomorrow",
    "Project discussion",
    "Call me tonight",
    "Assignment submission",
    "Meeting at 5 PM",
    "Happy birthday",
    "See you in class",
    "Dinner tonight",
    "Can we talk",
    "Your interview is scheduled",
    "Please submit report"
]


labels = [
    1,1,1,1,1,1,1,1,
    0,0,0,0,0,0,0,0,0,0,0,0
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)


X_train,X_test,y_train,y_test = train_test_split(X,labels,test_size=0.25,random_state=42)


model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

test_data = vectorizer.transform(['Congrats,you won!'])
prediction = model.predict(test_data)

print('is Spam:',prediction[0])

# classification report
print(classification_report(y_test,y_pred))

# confusion matrix
cm = confusion_matrix(y_test,y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()


# accuracy score
print('Actual:',y_test)
print('Predicted:',y_pred)
print(accuracy_score(y_test,y_pred))
