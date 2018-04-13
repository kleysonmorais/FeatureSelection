#------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   Correlation-Based Feature Selection-CFS with Python
#   April, 2018
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import cfs_pso
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data/mama.csv')
col = data.columns
y = data.diagnosis                          
list = ['Unnamed: 32','id','diagnosis']
X = data.drop(list,axis = 1)

B, M = y.value_counts()
print('Number of Benign: ',B)
print('Number of Malignant : ',M)

classe = cfs_pso.cfs_pso(np.asarray(X), np.asarray(y), 30, 5)
cost, pos = classe.cfspso()
print(pos)

# pos = np.array([1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0])

aux = np.asarray(X)
if np.count_nonzero(pos) == 0:
    X_subset = aux
else:
    X_subset = aux[:,pos==1]

# ORIGINAL
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# data train 70 % and test 30 %
x_train, x_test, y_train, y_test = train_test_split(X_subset, y, test_size=0.3, random_state=42)

clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(X_train,Y_train)
ac = accuracy_score(Y_test,clf_rf.predict(X_test))
print('Acurácia Original (', X.shape[1] ,' atributos) é: ', ac*100,'%')

clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(x_train,y_train)
ac = accuracy_score(y_test,clf_rf.predict(x_test))
print('Acurácia após CFS-PSO (', X_subset.shape[1] ,' atributos) é: ', ac*100,'%')