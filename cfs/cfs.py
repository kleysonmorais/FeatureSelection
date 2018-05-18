#------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   April, 2018
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

# from searchBuffer import *
from cfs.searchBuffer import BufferController
import pandas as pd
import numpy as np
import csv

def divideset(feature1, feature2, value):
    """
    Esta função serve para selecionar apenas as linhas da feature2, onde o valor na mesma linha
    da feature1 seja igual ao valor informado, no caso, value.

    Input
    ----------
    feature1: Coluna de atributo primária
    feature2: Coluna de atributo secundária
    value: Valor de seleção

    Output
    ----------
    set1: Subconjunto da feature2
    """
    set1 = []
    for item in range(len(feature1)):
        if feature1[item] == value:
            set1.append(feature2[item])
    return set1

def uniquecounts(feature):
    """
    Essa função irá contar a ocorrência de classes em um determinado conjunto de dados

    Input
    ----------
    feature: Coluna de interesse

    Output
    ----------
    results: Contador de classes da coluna
    """
    results = {}
    for row in feature:
        if row not in results:
            results[row] = 0
        results[row]+=1
    return results

def entropy(feature):
    """
    Esta função realiza o cálculo da entropia

    Input
    ----------
    feature: Atributo de interesse

    Output
    ----------
    ent: Resultado do cálculo da entropia, onde ent = - p(+)*log2(p(+)) - p(-)*log2(p(-))
    """
    from math import log
    log2 = lambda x:log(x)/log(2) # Propriedade logarítmica
    results = uniquecounts(feature) # função uniquicounts para contar as classes do conjunto.
    ent = 0.0
    for r in results.keys():
        p = float(results[r])/len(feature)
        ent = ent - p*log2(p) # Calculo de Entropia
    return ent

def meritoBuffer(data, atributo_classificador, particula, nome_base_dados):
    buffer = BufferController().search_buffer(particula, nome_base_dados)
    if buffer == None:
        m = merito(data,atributo_classificador)
        BufferController().save_buffer(particula, m, nome_base_dados)
        return m
    else:
        return buffer

def merito(data, atributo_classificador):
    """
    Esta função calcula o mérito da 'data' informada dada a classe 'atributo_classificador', onde
    merito = (k * rcf)/sqrt(k+k*(k-1)*rff)
    rcf = (1/k)*sum(is(fi,y)) for all fi in X
    rff = (1/(k*(k-1)))*sum(is(fi,fj)) for all fi and fj in X

    Input
    ----------
    data: subconjunto de features
    atributo_classificador: atributo classe

    Output
    ----------
    merito: quanto menor o mérito, melhor sua pontuação
    """
    n_rows, n_features = data.shape # Retorna o número de linhas e colunas
    rcf = 0
    rff = 0

    for i in range(n_features):
        fi = data[:, i] # Isolando coluna 'i'
        rcf += incerteza_simetrica(fi, atributo_classificador) # Calculando incerteza entre atributo e classe
        for j in range(n_features):
            if j > i:
                fj = data[:, j] # Isolando coluna 'j'
                rff += incerteza_simetrica(fi, fj) # Calculando incerteza entre atributo e atributo
        
    rff *= 2
    merito = rcf / np.sqrt(n_features + rff) # Simplificação da expressão
    return merito

def incerteza_simetrica(f1, f2):
    """
    Enta função calcula a incerteza simétrica, onde is(f1,f2) = 2*GanhoInformação(f1,f2)/(Entropia(f1)+Entropia(f2))
    
    Input
    ----------
    f1: feature para comparação
    f2: feature para comparação
    
    Output
    ----------
    incerteza: retorna a incerteza simétrica
    """
 
    # Calculando o Ganho, ganho = gi(f1,f2)
    ganho = ganho_informacao(f1, f2)
    # Entropia de f1
    ent1 = entropy(f1)
    # Entropia de f2
    ent2 = entropy(f2)

    incerteza = (2*ganho)/(ent1+ent2)

    return incerteza
    
def ganho_informacao(feature1, feature2):
    """
    Essa função calcula o ganho de um atributo em relação à outro atributo
    
    Input
    ----------
    feature1: feature para comparação
    feature2: feature para comparação
    
    Output
    ----------
    ganho: retorna o ganho de informação
    """
    # Recebendo a entropia do atributo classificador
    ganho = entropy(feature2)

    # Verificando valores presentes na coluna do atributo informado
    dicionario = uniquecounts(feature1)

    # Iterando sob cada valor encontrado
    for item in dicionario:
        valor = str(item) # Convertendo Para String
        set1 = divideset(feature1, feature2, valor) # Isolando o valor
        ent = entropy(set1) # Calculando a entropia do atributo informado em relação ao atributo classificador
        aux = (len(set1)/len(feature1))*ent
        ganho = ganho - aux # Somatória das entropias (parte da fórmula do ganho de informação)
    
    return ganho
    
def cfs(data, atributo_classificador):
    """
    Esta função usa uma heurística baseada em correlação para avaliar o valor de atributos que é chamada CFS
    
    Input
    ----------
    data: subconjunto de features
    atributo_classificador: atributo classe

    Output
    ----------
    np.array(FEATURE): retorna o subconjunto resultado da filtragem
    """

    n_rows, n_features = data.shape
    
    # Subconjunto de features
    FEATURE = []
    
    # Histórico de mérito
    MERITO = []

    # O algoritmo utiliza geração adiante
    while True:
        # Valor pequeno para substituição do menor mérito
        merit = -100000000000
        # Variável auxiliar
        idx = -1
        # Iterações para formação de subgrupos de features
        for i in range(n_features):
            if i not in FEATURE:
                FEATURE.append(i)
                t = merito(data[:, FEATURE], atributo_classificador)
                if t > merit:
                    merit = t
                    idx = i
                FEATURE.pop()
        FEATURE.append(idx)
        print (merit)
        MERITO.append(merit)
        # Critério de parada da execução
        if len(MERITO) > 5:
            print("*")
            if MERITO[len(MERITO)-1] <= MERITO[len(MERITO)-2]:
                print("**")
                if MERITO[len(MERITO)-2] <= MERITO[len(MERITO)-3]:
                    print("***")
                    if MERITO[len(MERITO)-3] <= MERITO[len(MERITO)-4]:
                        print("****")
                        if MERITO[len(MERITO)-4] <= MERITO[len(MERITO)-5]:
                            print("*****")
                            break

    return np.array(FEATURE) # Cria uma nova data com as features selecionadas

if __name__ == '__main__':
    # #Leitura data
    # dat = pd.read_csv('data/data4.csv')
    # tuples = [tuple(x) for x in dat.values]

    # data = np.asarray(tuples)

    # # Importante informar no segundo parâmetro qual é o atributo classificador, no caso, o último    
    # selection_feature = cfs(data, data[:,-1])
    # print(selection_feature)
    print("teste")    
