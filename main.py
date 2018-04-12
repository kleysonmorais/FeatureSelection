import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization library  
import matplotlib.pyplot as plt
import cfs
import time
from subprocess import check_output
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score,confusion_matrix
from sklearn.metrics import accuracy_score

data = pd.read_csv('data/mama.csv')
col = data.columns
y = data.diagnosis                          # M or B 
list = ['Unnamed: 32','id','diagnosis']
x = data.drop(list,axis = 1)

B, M = y.value_counts()
print('Number of Benign: ',B)
print('Number of Malignant : ',M)

# features = cfs.cfs(np.asarray(x), np.asarray(y))
# selection_features = [24, 8, 20, 0, 4, 1]
# print(features) # [24  8  20  0  4  1]

remove_features = [2,3,5,6,7,9,10,11,12,13,14,15,
                    16,17,18,19,21,22,23,25,26,27,28,29,30]
x_1 = x.drop(x.columns[[2,3,5,6,7,9,10,11,12,13,14,15,
                    16,17,18,19,21,22,23,25,26,27,28,29]], axis=1)        # do not modify x, we will use it later 

# split data train 70 % and test 30 %
# x_train, x_test, y_train, y_test = train_test_split(x_1, y, test_size=0.3, random_state=42)

# ORIGINAL
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

#random forest classifier with n_estimators=10 (default)
clf_rf = RandomForestClassifier(random_state=43)      
clr_rf = clf_rf.fit(x_train,y_train)

ac = accuracy_score(y_test,clf_rf.predict(x_test))
print('Accuracy is: ', ac)
# cm = confusion_matrix(y_test,clf_rf.predict(x_test))
# sns.heatmap(cm,annot=True,fmt="d")

