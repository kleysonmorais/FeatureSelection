import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pyswarms as ps
import cfs
from sklearn import linear_model
from sklearn.datasets import make_classification

# data = pd.read_csv('data/data4min.csv')
# col = data.columns
# y = np.asarray(data.Churn_Status)

# list = ['Churn_Status']
# X = np.asarray(data.drop(list,axis = 1))


class cfs_pso:
    X = []
    y = []
    n_particles = 0
    iteracao = 0

    def __init__(self, X_in, y_in, dimensions, n_particles):
        self.X = X_in
        self.y = y_in
        self.dimensions = dimensions
        self.n_particles = n_particles

    def search_buffer(self, m):
        arquivo = open('buffer/buffer.txt', 'r')
        m_string = "[" + " ".join(str(x) for x in m) + "]"
        for linha in arquivo:
            aux = linha[0:61]
            if m_string == aux:
                aux2 = linha[62:-1]
                print('Retornando Merito Encontrado')
                return float(aux2)
        print('Merito não encontrado')
        arquivo.close()
        return None
        

    def save_buffer(self, m, merito):
        arquivo = open('buffer/buffer.txt', 'r') 
        conteudo = arquivo.readlines()
        
        texto = '[' + ' '.join(str(x) for x in m) + '] ' + repr(merito) + '\n'
        print('Salvando Novo Mérito')
        conteudo.append(texto)   
        
        arquivo = open('buffer/buffer.txt', 'w')
        arquivo.writelines(conteudo)   

        arquivo.close

    def classifica_merito(self, m):
        # print(m)
        # self.test_buffer(m)
        # print(self.X)

        buffer = self.search_buffer(m)
        if buffer == None:
            if np.count_nonzero(m) == 0:
                X_subset = self.X
            else:
                X_subset = self.X[:,m==1]
            # print(X_subset.shape)
            merito = cfs.merito(X_subset, self.y)
            self.save_buffer(m, merito)
            # print(merito)
            return merito
        else:
            return buffer

    def k(self, x):
        self.iteracao+=1
        print("Iteração: ", self.iteracao)
        n_particles = x.shape[0]
        j = [self.classifica_merito(x[i]) for i in range(n_particles)]
        return np.array(j)

    def cfspso(self):
        # X = X_in
        # y = y_in
        print('particula: ', self.n_particles)
        options = {'c1': 0.5, 'c2': 0.5, 'w':0.9, 'k': self.n_particles, 'p':2}

        # dimensions = 10
        optimizer = ps.discrete.BinaryPSO(n_particles=self.n_particles, dimensions=self.dimensions, options=options)

        cost, pos = optimizer.optimize(self.k, print_step=10, iters=5, verbose=2)
        return cost, pos

# def main():

#     options = {'c1': 0.5, 'c2': 0.5, 'w':0.9, 'k': 5, 'p':2}

#     dimensions = 10
#     optimizer = ps.discrete.BinaryPSO(n_particles=5, dimensions=dimensions, options=options)

#     cost, pos = optimizer.optimize(k, print_step=100, iters=1000, verbose=2)
#     print(cost)
#     print(pos)


# if __name__ == '__main__':
#     main()