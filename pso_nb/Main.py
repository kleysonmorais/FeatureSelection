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

import numpy as np 
import pandas as pd

data = pd.read_csv('../data/mama.csv')
col = data.columns
y = data.diagnosis                          
list = ['Unnamed: 32','id','diagnosis']
X = data.drop(list,axis = 1)

tamPopulacao = 1
geracoes = 1
ac = AvaliadorController(X, y)

dadosModel = DadosModel(X, y)
enxame = EnxameModel()
ec = EnxameController(dadosModel)
ec.criarEnxame(enxame, tamPopulacao)

for i in range(geracoes):
    ec.atualizaEnxame(enxame)

ac.allClassifiers(enxame._melhorPosicaoGlobal)


