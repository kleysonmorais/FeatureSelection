import pandas as pd
import csv

# Função para leitura de CSV
def getData(text):
    with open(text, 'rb') as ficheiro:
        reader = csv.reader(ficheiro)
        return reader

# Esta função serve para separar o conjunto em duas partes
# data: é referente aos dados
# atributo: é referente à alguma coluna específica
# value: valor a ser consultado, esse valor será usado para separar o conjunto
def divideset(data, atributo, value):
    split_function = None # função de acordo com a situação.
    if isinstance(value,int) or isinstance(value,float):
        split_function = lambda row:row[atributo]&amp;amp;amp;amp;amp;amp;gt;value # se o valor é int ou float.
    else:
        split_function = lambda row:row[atributo]==value # se for string

    set1 = [row for row in data if split_function(row)]
    set2 = [row for row in data if not split_function(row)]
    return (set1, set2)

# Essa função irá contar a ocorrência de classes em um determinado conjunto de dados
# O parâmetro coluna deve receber o valor da coluna que deseja-se contar
def uniquecounts(data, atributo):
    results = {}
    for row in data:
        # r = row[-1] # Ultima coluna 
        r = row[atributo] # Coluna onde se encontra a classe
        if r not in results:
            results[r] = 0
        results[r]+=1
    return results

# Função que calcula a entropia
def entropy(data, atributo_classificador):
    from math import log
    log2 = lambda x:log(x)/log(2) # Propriedade logarítmica
    results = uniquecounts(data, atributo_classificador) # função uniquicounts para contar as classes do conjunto.
    ent = 0.0
    for r in results.keys():
        p = float(results[r])/len(data)
        ent = ent - p*log2(p) # Calculo de Entropia
    return ent

# Em cada iteração do algoritmo é escolhido o atributo que apresente uma maior ganho.
# Essa função calcula o ganho de um atributo em relação ao atributo classificador
def ganho_informacao(data, atributo, atributo_classificador):

    # Recebendo a entropia do atributo classificador
    ganho = entropy(data, atributo_classificador)

    # Verificando valores presentes na coluna do atributo informado
    dicionario = uniquecounts(data, atributo)
    # Iterando sob cada valor encontrado
    for item in dicionario:
        valor = str(item) # Convertendo Para String
        set1, set2 = divideset(data, atributo, valor) # Isolando o valor
        ent = entropy(set1, atributo_classificador) # Calculando a entropia do atributo informado em relação ao atributo classificador
        
        ganho = ganho - ((len(set1)/len(data))*ent) # Somatória das entropias (parte da fórmula do ganho de informação)
    
    print("Ganho: ", ganho)
    return ganho
    
    
    # set1, set2 = divideset(data, atributo, x[0])
    

if __name__ == '__main__':
    #Leitura data
    # data = getData('data/data1.csv')
    # data = pd.read_csv('data/data1.csv')
    # tuples = [tuple(x) for x in data.values]
    # datal = list(data)
    # print (tuples)
    # my_data=[['slashdot','USA','yes',18,'None'],
    # ['google','France','yes',23,'Premium'],
    # ['digg','USA','yes',24,'Basic'],
    # ['kiwitobes','France','yes',23,'Basic'],
    # ['google','UK','no',21,'Premium'],
    # ['(direct)','New Zealand','no',12,'None'],
    # ['(direct)','UK','no',21,'Basic'],
    # ['google','USA','no',24,'Premium'],
    # ['slashdot','France','yes',19,'None'],
    # ['digg','USA','no',18,'None'],
    # ['google','UK','no',18,'None'],
    # ['kiwitobes','UK','no',19,'None'],
    # ['digg','New Zealand','yes',12,'Basic'],
    # ['slashdot','UK','no',21,'None'],
    # ['google','UK','yes',18,'Basic'],
    # ['kiwitobes','France','yes',19,'Basic']]

    # # Calculo de Entropia
    # x = entropy(tuples)
    # print (uniquecounts(my_data, -1))
    # print (uniquecounts(tuples, 1))

    treino = [
    ['D1', 'Sol', 'Quente', 'Elevada', 'Fraco', 'Não'],
    ['D2', 'Sol', 'Quente', 'Elevada', 'Forte', 'Não'],
    ['D3', 'Nuvens', 'Quente', 'Elevada', 'Fraco', 'Sim'],
    ['D4', 'Chuva', 'Ameno', 'Elevada', 'Fraco', 'Sim'],
    ['D5', 'Chuva', 'Fresco', 'Normal', 'Fraco', 'Sim'],
    ['D6', 'Chuva', 'Fresco', 'Normal', 'Forte', 'Não'],
    ['D7', 'Nuvens', 'Fresco', 'Normal', 'Fraco', 'Sim'],
    ['D8', 'Sol', 'Ameno', 'Elevada', 'Fraco', 'Não'],
    ['D9', 'Sol', 'Fresco', 'Normal', 'Fraco', 'Sim'],
    ['D10', 'Chuva', 'Ameno', 'Normal', 'Forte', 'Sim'],
    ['D11', 'Sol', 'Ameno', 'Normal', 'Forte', 'Sim'],
    ['D12', 'Nuvens', 'Ameno', 'Elevada', 'Forte', 'Sim'],
    ['D13', 'Nuvens', 'Quente', 'Normal', 'Fraco', 'Sim'],
    ['D14', 'Chuva', 'Ameno', 'Elevada', 'Forte', 'Não']
    ]

    # x = entropy(treino, 5)
    # print(x)

    ganho_informacao(treino, 2, 5)

