#------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   Genetic Algorithm with Correlation-Based Feature Selection-CFS
#   April, 2018
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+
from random import randint

class genetic:

    populacao = []
    qtd_gerecao = 0
    qtd_populacao = 0

    def __init__(self, qtd_populacao, qtd_gerecao):
        self.qtd_populacao = qtd_populacao
        self.qtd_gerecao = qtd_gerecao

    def gerarPopulacao(self):
        # print("Qtd: ", self.qtd_populacao)
        for item in range(self.qtd_populacao):
            self.populacao.append(self.criarCromossomo())
        # print("População: ", self.populacao)

    def criarCromossomo(self):
        cromossomo = []
        for item in range(30):
            cromossomo.append(randint(0, 1))
        print("Cromossomo: ", cromossomo)
        return cromossomo

    def fitness(self):
        fitness = []
        
        for cromossomo in range(self.populacao):
            # CFS cromossomo
            fit = cfs()
            fitness.append(fit)
        for i in ran-ge(self.qtd_populacao/2):
            posicao = 0
            maior = -10000000000
            for idx in range(fitness):
                if filter[idx] > maior:
                    posicao = idx 
                    maior = filter[idx]
            fitness.remove(posicao)
            self.populacao.remove(posicao)

    # def crossover(self):


    # def mutacao(self):

if __name__ == '__main__':
    genetic(10, 10).gerarPopulacao()

    