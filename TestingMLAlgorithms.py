# Testing a range of ML algorithms against model to determine best accuracy.

# Imports
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd
# Visulization
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

# Algorithms
from sklearn.linear_model import LogisticRegression # LR
from sklearn.tree import DecisionTreeClassifier # DT
from sklearn.naive_bayes import BernoulliNB # NB
from sklearn.svm import SVC # SVM
from sklearn.ensemble import RandomForestClassifier # RF


# Data preperation
dataset = pd.read_csv("urldata.csv") 
y = dataset["label"] 
urls = dataset["url"] 
vectorizer = TfidfVectorizer() 
X = vectorizer.fit_transform(urls)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

# LR test
lr_model = LogisticRegression(max_iter=1000)	
lr_model.fit(X_train, y_train) 
y_pred = lr_model.predict(X_test)
print("Logistic Regression: Accuracy")
print(classification_report(y_test, y_pred)) # 96%

# RF Test
rf_model = RandomForestClassifier(n_estimators=20, max_depth=20, random_state=42)	
rf_model.fit(X_train, y_train) 
y_pred = rf_model.predict(X_test)
print("Random Forest: Accuracy")
print(classification_report(y_test, y_pred)) # 82%

# SVM Test
svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)
print("Support Vector Machine: Accuracy")
print(classification_report(y_test, y_pred)) # 98%

# NB Test
nb_model = BernoulliNB()
nb_model.fit(X_train, y_train)
y_pred = nb_model.predict(X_test)
print("Naive Bayes: Accuracy")
print(classification_report(y_test, y_pred)) # 95%

# DT Test
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
y_pred = dt_model.predict(X_test)
print("Decision Tree: Accuracy")
print(classification_report(y_test, y_pred)) # 97%


# Confusion Matrix for LR
#confusionMatrix = metrics.confusion_matrix(y_test, y_pred) # create cm
#sns.heatmap(confusionMatrix, cmap="Blues", annot=True) # Display heatmap of cm
#plt.xticks(np.arange(2)+0.5, ["Good", "Bad"])
#plt.yticks(np.arange(2)+0.5, ["Good", "Bad"])
#plt.xlabel("Predicted")
#plt.ylabel("Actual")
#plt.show()
