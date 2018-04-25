from Models import *

import scipy.spatial as spp
import numpy as np

#===============================================================================
# Binary Particle controller
#===============================================================================
class BinaryParticleController:
    
    _solucao = None
    
    def __init__(self, solucao):
        self._solucao = solucao

    def initParticle(self, model, dimencao):
        # Create posicao array
        model._posicao = np.random.randint(2, size = dimencao)
        # Create Velocity array
        model._velocidade = np.random.randint(2, size = dimencao)
        # Save best Position so far as current Position
        model._melhorPosicao = model._posicao
        # self.updateFitness(model)

    def updateFitness(self, model):
        # Get Differences of vector
        hdist = spp.distance.hamming(model._posicao, self._solucao)
        # Save it as best posicao if its better than previous best
        if (hdist < model._fitness) or (model._fitness is None):
            model._melhorPosicao = np.copy(model._posicao)
            model._fitness = hdist

    def updatePosition(self, model):
        # VELOCITY NEEDS TO BE CONSTRICTED WITH VMAX
        # Get random coefficients e1 & e2
        c = 2.5
        e1 = np.random.rand()
        e2 = np.random.rand()
        vmax = 6
        # Apply equation to each component of the velocidade, add it to corresponding posicao component
        for i, velocidade in enumerate(model._velocidade):
#            velocidade = 0.72984 * (velocidade + c * e1 * (model._melhorPosicao[i] - model._posicao[i]) + c * e2 * (model._nbBestPosition[i] - model._posicao[i]))
            velocidade = velocidade + c * e1 * (model._melhorPosicao[i] - model._posicao[i]) + c * e2 * (model._nbBestPosition[i] - model._posicao[i])
            if abs(velocidade) > vmax and abs(velocidade) is velocidade: 
                velocidade = vmax
            elif abs(velocidade) > vmax:
                velocidade = -vmax
            velocidade = self.sigmoid(velocidade)
#            print "vel:", velocidade
            if np.random.rand(1) < velocidade:
                model._posicao[i] = 1
            else:
                model._posicao[i] = 0
            
    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-(x)))

#===============================================================================
# Swarm Controller
#===============================================================================
class SwarmController:    

    particulaController = None
    _vizinhancaController = None
    
    def __init__(self, solucao):
        self.particulaController = BinaryParticleController(solucao)
        self._vizinhancaController = VizinhancaController()
    
    def initSwarm(self, swarm, topology = "gbest" , nParticulas = 1, dimencao = 1):
        # Criar Enxame
        for i in range(nParticulas):
            novaParticula = ParticleModel()
            self.particulaController.initParticle(novaParticula, dimencao)
            # print(novaParticula._posicao)
            swarm._particulas.append(novaParticula)    
        swarm._vizinhanca = self._vizinhancaController.inicializarVizinhaca(swarm, topology)
        self.updateSwarmBestPosition(swarm)
            

    def updateSwarmBestPosition(self, swarm):
        # Find swarm best posicao and save it in swarm
        for nb in swarm._vizinhanca:
            self._vizinhancaController.updateVizinhancaMelhorPosicao(nb)
            if swarm._melhorPosicaoFitness is None or nb._melhorPosicaoFitness < swarm._melhorPosicaoFitness:
                swarm._melhorPosicaoFitness = nb._melhorPosicaoFitness
                swarm._melhorPosicao =  np.copy(nb._melhorPosicao)
    
    # Update all particles in the swarm 
    def updateSwarm(self, swarm):
        for curParticle in swarm._particulas:
            self.particulaController.updatePosition(curParticle)
            self.particulaController.updateFitness(curParticle)
        self.updateSwarmBestPosition(swarm)
        
        
#===============================================================================
# Neighborhood Controller
#===============================================================================
class VizinhancaController:    

    def inicializarVizinhaca(self, swarm, topology = "gbest"):
        if topology is "gbest":
            return [VizinhancaModel(swarm._particulas)]
        elif topology is "lbest":
            vizinhanca = []
            for idx, curParticle in enumerate(swarm._particulas):
                previousParticle = None
                nextParticle = None
                if idx is 0:
                    # Previous is last, next is next
                    nextParticle = swarm._particulas[idx + 1]
                    previousParticle = swarm._particulas[len(swarm._particulas) - 1]
                elif idx is len(swarm._particulas) - 1:
                    # Previous is previous, next is first
                    nextParticle = swarm._particulas[0]
                    previousParticle = swarm._particulas[idx - 1]
                else:
                    # Previous is previous, next is next
                    nextParticle = swarm._particulas[idx + 1]
                    previousParticle = swarm._particulas[idx - 1]
                vizinhanca.append(VizinhancaModel([previousParticle, curParticle, nextParticle]))
            return vizinhanca

    def updateVizinhancaMelhorPosicao(self, model):
        # Find the best one in the NB
        for curParticle in model._particulas:
            if model._melhorPosicaoFitness is None or (curParticle._fitness < model._melhorPosicaoFitness and curParticle._fitness is not None):
                model._melhorPosicaoFitness = curParticle._fitness
                model._melhorPosicao = np.copy(curParticle._melhorPosicao)

        # Save nb best posicao in particles nbBestPosition 
        for curParticle in model._particulas:
            curParticle._nbBestPosition = np.copy(model._melhorPosicao)