from Models import *
from Controller import *

import numpy as np
import pylab as pyl

class PSOGeneric():

    _plotPoints = []
    
    _topology       = None
    _dimensao     = None
    _tamPopulacao   = None
    _geracoes    = None

    def __init__(self, topology):
        self._plotPoints = None
        self._topology = topology
    
    def printResult(self):
        print ("PSOProblem Result:")

    def plotResults(self):
        x = []
        y = []
        for (generation, fitness) in self._plotPoints:
            x.append(fitness)
            y.append(generation)
        pyl.plot(x, y)
        
        pyl.grid(True)
        pyl.title('Optimizing %dD Float Vector (Topology: %s) ' % (self._dimensao, self._topology))
        pyl.xlabel('Fitness (f)')
        pyl.ylabel('Generation (i)')
        pyl.savefig('simple_plot')

        pyl.show()

class CBPSOProblem(PSOGeneric):

    def __init__(self, topology="gbest"):
        print("\nBPSO")
        
        solution5 = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
        solucao  = solution5

        self._tamPopulacao = tamPopulacao = 50
        self._dimensao = dimensoes  = len(solucao)
        self._geracoes = geracoes = 100
        self._topology = topology
        
        print("Tamanho da População: ", tamPopulacao)
        print("Total de Dimensões: ", dimensoes)
        print("Quantidade de Gerações: ", geracoes)
        print("Topology: ", topology)

        enxame   = EnxameModel()
        ec      = EnxameController(solucao)
        ec.initEnxame(enxame, topology, tamPopulacao, dimensoes)
        
        fitness = 1
        idx = 0
        for i in range(geracoes):
            ec.updateEnxame(enxame)
            if enxame._melhorPosicaoFitness < fitness:
                fitness = enxame._melhorPosicaoFitness
                idx = i
            gen = i+1
            fit = dimensoes - (dimensoes * enxame._melhorPosicaoFitness)
            self._plotPoints.append( (gen, fit) )
            print ("Generation", i+1,"\t-> BestPos:", enxame._melhorPosicao, "\tBestFitness:", enxame._melhorPosicaoFitness)
        
        print ("\n===================================================================")
        print ("Dimensions:\t", dimensoes)
        print ("Solution:\t", np.array(solucao))
        print ("Best Result:\t", enxame._melhorPosicao)
        print ("Best Fitness:\t", 1 - enxame._melhorPosicaoFitness, "in %d" % idx, " iteration out of %d" % geracoes)
        print ("Number of bits out of place: %d" % (dimensoes * enxame._melhorPosicaoFitness))
        print ("===================================================================")
        
    def plotResults(self):
        x = []
        y = []
        for (generation, fitness) in self._plotPoints:
            x.append(fitness)
            y.append(generation)