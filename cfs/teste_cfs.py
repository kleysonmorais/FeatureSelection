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
import cfs
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data/mama.csv')
col = data.columns
y = data.diagnosis                          
list = ['Unnamed: 32','id','diagnosis']
x = data.drop(list,axis = 1)

B, M = y.value_counts()
print('Number of Benign: ',B)
print('Number of Malignant : ',M)

features = cfs.cfs(np.asarray(x), np.asarray(y)) 
# // Features Selecionadas = [24, 8, 20, 0, 4, 1]

# Removendo Atributos Não Selecionados
x_1 = x.drop(x.columns[[2,3,5,6,7,9,10,11,12,13,14,15,
                    16,17,18,19,21,22,23,25,26,27,28,29]], axis=1)

# ORIGINAL
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# data train 70 % and test 30 %
x_train, x_test, y_train, y_test = train_test_split(x_1, y, test_size=0.3, random_state=42)

clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(X_train,Y_train)
ac = accuracy_score(Y_test,clf_rf.predict(X_test))
print('Acurácia Original (', x.shape[1] ,' atributos) é: ', ac*100,'%')

clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(x_train,y_train)
ac = accuracy_score(y_test,clf_rf.predict(x_test))
print('Acurácia após CFS (', x_1.shape[1] ,' atributos) é: ', ac*100,'%')
