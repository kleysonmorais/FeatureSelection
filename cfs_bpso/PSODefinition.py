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
#        print self._plotPoints
        x = []
        y = []
        for (generation, fitness) in self._plotPoints:
            x.append(fitness)
            y.append(generation)
#            print "%.4f" % (fitness)
        pyl.plot(x, y)
        
        pyl.grid(True)
        pyl.title('Optimizing %dD Float Vector (Topology: %s) ' % (self._dimensao, self._topology))
        pyl.xlabel('Fitness (f)')
        pyl.ylabel('Generation (i)')
        pyl.savefig('simple_plot')

        pyl.show()

#---- Continuous Binary PSO Problem
class CBPSOProblem(PSOGeneric):

    def __init__(self, topology="gbest"):
        print("\nBPSO")
        # Problem parameters
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

        # Swarm Initialization
        swarm   = SwarmModel()
        sc      = SwarmController(solucao)
        sc.initSwarm(swarm, topology, tamPopulacao, dimensoes)
        
        # Output Results
        fitness = 1
        idx = 0
        for i in range(geracoes):
            sc.updateSwarm(swarm)
            if swarm._bestPositionFitness < fitness:
                fitness = swarm._bestPositionFitness
                idx = i
            gen = i+1
            fit = dimensoes - (dimensoes * swarm._bestPositionFitness)
            self._plotPoints.append( (gen, fit) )
#            self._plotPoints += (i+1, 1 - swarm._bestPositionFitness)
            print ("Generation", i+1,"\t-> BestPos:", swarm._bestPosition, "\tBestFitness:", swarm._bestPositionFitness)
        
#         print ("\n===================================================================")
#         print ("Dimensions:\t", dimensoes)
#         print ("Solution:\t", np.array(solucao))
#         print ("Best Result:\t", swarm._bestPosition)
#         print ("Best Fitness:\t", 1 - swarm._bestPositionFitness, "in %d" % idx, " iteration out of %d" % geracoes)
#         print ("Number of bits out of place: %d" % (dimensoes * swarm._bestPositionFitness))
#         print ("===================================================================")
        
    def plotResults(self):
#        print self._plotPoints
        x = []
        y = []
        for (generation, fitness) in self._plotPoints:
            x.append(fitness)
            y.append(generation)
#            print "%d" % (fitness)