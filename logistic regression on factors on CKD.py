# -*- coding: utf-8 -*-
"""logistic.ipynb의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eS0zVJjCNleILHKsXP0ovJcuiXEC8z1B
"""

import pandas as pd
import numpy as np
import pandas as pd
import sklearn
 
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve
import statsmodels.api as sm
import matplotlib.pyplot as plt
import time


#loading data

 
from google.colab import files

uploaded = files.upload()

import pandas as pd
import io

df = pd.read_csv(io.BytesIO(uploaded['chronic_kidney_disease_full - Copy.csv']))

print(df.shape)
print(df.head())

#drop NA
df = df.dropna()



#drop columns not needed.

print(list(df.columns))
df.drop(df.columns[[0, 3, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]], axis=1, inplace=True)
print(df)

# one hot encoding

df = pd.get_dummies(df, columns = ['rbc', 'ba','sod','pot','htn','appet'])
print(df)

#Creating Features Array
X = df.iloc[:,1:]
X.head ()

Y = data.iloc[:,0]

# split the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)


# Creating the Logistic Regression classifier from sklearn toolkit
classifier = LogisticRegression(solver='lbfgs',random_state=0)
classifier.fit(X_train, Y_train)

# Testing
predicted_y = classifier.predict(X_test)
predicted_y

for x in range(len(predicted_y)):
    if (predicted_y[x] == 1):
        print(x, end="\t")



#Verifying Accuracy
print('Accuracy: {:.2f}'.format(classifier.score(X_test, Y_test)))

