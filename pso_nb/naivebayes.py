#------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   June, 2018
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

data = pd.read_csv('../data/sportEdit.csv')
col = data.columns
y = data.Label                          
list = ['Label', 'TextID', 'URL']
X = data.drop(list,axis = 1)

print(col)

ax = sns.countplot(y, label="Count")      
objective, subjective = y.value_counts()
print('Number of Objective: ', objective)
print('Number of Subjective : ', subjective)

print(X.shape)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
classificador = GaussianNB().fit(x_train,y_train)
ac = accuracy_score(y_test, classificador.predict(x_test))

f1 = f1_score(y_test, classificador.predict(x_test), average='micro')  

print("Acurácia: ", ac*100)
print("F1 Score: ", f1*100)
