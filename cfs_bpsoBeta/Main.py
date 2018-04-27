from Models import *
from Controller import *

import numpy as np 
import pandas as pd

data = pd.read_csv('../data/mama.csv')
col = data.columns
y = data.diagnosis                          
list = ['Unnamed: 32','id','diagnosis']
X = data.drop(list,axis = 1)

tamPopulacao = 10
nAtributos = 30
geracoes = 10

enxame = EnxameModel()
ec = EnxameController()
ec.criarEnxame(enxame, tamPopulacao, nAtributos)

