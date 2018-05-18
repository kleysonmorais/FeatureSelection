import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

from Models import *
from Controller import *
from benchmark.avaliador import AvaliadorController


nome_base_dados = "cancer"

data = pd.read_csv('../data/'+nome_base_dados+'.csv')
list = ['classe']
y = data.classe
X = data.drop(list,axis = 1)
# print(y.value_counts())

# tamPopulacao = 40
# geracoes = 100
ac = AvaliadorController(X, y)
ac.allClassificadores()

# dadosModel = DadosModel(X, y)
# enxame = EnxameModel()
# # ec = EnxameController(dadosModel, nome_base_dados)
# ec = EnxameController(dadosModel, avaliador=ac, tipo="wrappers")
# ec.criarEnxame(enxame, tamPopulacao)

# for i in range(geracoes):
#     ec.atualizaEnxame(enxame)

# ac.allClassifiers(enxame._melhorPosicaoGlobal)



# ax = sns.countplot(y,label="Count")
# data_dia = y
# data = X
# data_n_2 = (data - data.mean()) / (data.std())              # standardization
# data = pd.concat([y,data_n_2.iloc[:,0:10]],axis=1)
# data = pd.melt(data,id_vars="classe",
#                     var_name="features",
#                     value_name='value')
# plt.figure(figsize=(10,10))
# sns.violinplot(x="features", y="value", hue="classe", data=data,split=True, inner="quart")
# plt.xticks(rotation=90)


# fig, ax = plt.subplots(figsize=(7, 7))
# sns.heatmap(X.corr(), annot=True, linewidths=.2, fmt= '.1f',ax=ax)

# plt.show()
# fig.savefig('temp.png', dpi=fig.dpi)

# sns.set(style="whitegrid", palette="muted")
# data_dia = y
# data = X
# data_n_2 = (data - data.mean()) / (data.std())              # standardization
# data = pd.concat([y,data_n_2.iloc[:,0:10]],axis=1)
# data = pd.melt(data,id_vars="classe",
#                     var_name="features",
#                     value_name='value')
# plt.figure(figsize=(8,10))
# tic = time.time()
# sns.swarmplot(x="features", y="value", hue="classe", data=data)

# plt.xticks(rotation=90)
# plt.show()
# data.savefig('temp.png', dpi=data.dpi)

# tamPopulacao = 10
# geracoes = 10
# features1 = np.array([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
# features = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# ac = AvaliadorController(X, y)
# ac.allClassifiers(features1)
# ac.allClassifiers(features)
# aux = np.asarray(X)
# if np.count_nonzero(features) == 0:
#     X_subset = aux
# else:
#     X_subset = aux[:,features==1]        
# print(X_subset)

# dadosModel = DadosModel(X, y)
# enxame = EnxameModel()
# ec = EnxameController(dadosModel)
# ec.criarEnxame(enxame, tamPopulacao)

# for i in range(geracoes):
#     ec.atualizaEnxame(enxame)

# ac.allClassifiers(enxame._melhorPosicaoGlobal)