#------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   June, 2018
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from Models import *
from Controller import *
from benchmark.avaliador import AvaliadorController
from Visualiza import *

import numpy as np 
import pandas as pd


data = pd.read_csv('../data/sportEdit.csv')
col = data.columns
y = data.Label                          
list = ['Label', 'TextID', 'URL']
X = data.drop(list,axis = 1)

tamPopulacao = 5
geracoes = 3
ac = AvaliadorController(X, y)

dadosModel = DadosModel(X, y)
enxame = EnxameModel()
ec = EnxameController(dadosModel, ac)
ec.criarEnxame(enxame, tamPopulacao)

for i in range(geracoes):
    print(i+1,"/",geracoes)
    ec.atualizaEnxame(enxame)

ac.allClassifiers(enxame._melhorPosicaoGlobal)


