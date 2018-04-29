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

    def initParticula(self, model, dimencao):
        # Create posicao array
        model._posicao = np.random.randint(2, size = dimencao)
        # Create Velocity array
        model._velocidade = np.random.randint(2, size = dimencao)
        # Save best Position so far as current Position
        model._melhorPosicao = model._posicao
        self.updateFitness(model)

    def updateFitness(self, model):
        # Get Differences of vector
        # hdist = spp.distance.hamming(model._posicao, self._solucao)
        hdist = np.random.randint(5, 52)
        # Save it as best posicao if its better than previous best
        if model._fitness is None:
            model._melhorPosicao = np.copy(model._posicao)
            model._fitness = hdist
        elif hdist < model._fitness:
            model._melhorPosicao = np.copy(model._posicao)
            model._fitness = hdist

    def updatePosicao(self, model):
        c = 2.5
        e1 = np.random.rand()
        e2 = np.random.rand()
        vmax = 6
        for i, velocidade in enumerate(model._velocidade):
            velocidade = velocidade + c * e1 * (model._melhorPosicao[i] - model._posicao[i]) + c * e2 * (model._nbBestPosition[i] - model._posicao[i])
            if abs(velocidade) > vmax and abs(velocidade) is velocidade: 
                velocidade = vmax
            elif abs(velocidade) > vmax:
                velocidade = -vmax
            velocidade = self.sigmoid(velocidade)
            if np.random.rand(1) < velocidade:
                model._posicao[i] = 1
            else:
                model._posicao[i] = 0
            
    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-(x)))

#===============================================================================
# enxame Controller
#===============================================================================

class EnxameController:    

    particulaController = None
    _vizinhancaController = None
    
    def __init__(self, solucao):
        self.particulaController = BinaryParticleController(solucao)
        self._vizinhancaController = VizinhancaController()
    
    def initEnxame(self, enxame, topology = "gbest" , nParticulas = 1, dimencao = 1):
        # Criar Enxame
        for i in range(nParticulas):
            novaParticula = ParticulaModel()
            self.particulaController.initParticula(novaParticula, dimencao)
            enxame._particulas.append(novaParticula)    
        enxame._vizinhanca = self._vizinhancaController.inicializarVizinhaca(enxame, topology)
        self.updateMelhorPosicaoEnxame(enxame)
            
    def updateMelhorPosicaoEnxame(self, enxame):
        # Find enxame best posicao and save it in enxame
        for nb in enxame._vizinhanca:
            self._vizinhancaController.updateVizinhancaMelhorPosicao(nb)
            if enxame._melhorPosicaoFitness is None or nb._melhorPosicaoFitness < enxame._melhorPosicaoFitness:
                enxame._melhorPosicaoFitness = nb._melhorPosicaoFitness
                enxame._melhorPosicao =  np.copy(nb._melhorPosicao)
    
    def updateEnxame(self, enxame):
        for curParticle in enxame._particulas:
            self.particulaController.updatePosicao(curParticle)
            self.particulaController.updateFitness(curParticle)
        self.updateMelhorPosicaoEnxame(enxame)
        
#===============================================================================
# Vizinhança Controller
#===============================================================================

class VizinhancaController:    

    def inicializarVizinhaca(self, enxame, topology = "gbest"):
        if topology is "gbest":
            return [VizinhancaModel(enxame._particulas)]
        elif topology is "lbest":
            vizinhanca = []
            for idx, curParticle in enumerate(enxame._particulas):
                previousParticle = None
                nextParticle = None
                if idx is 0:
                    nextParticle = enxame._particulas[idx + 1]
                    previousParticle = enxame._particulas[len(enxame._particulas) - 1]
                elif idx is len(enxame._particulas) - 1:
                    nextParticle = enxame._particulas[0]
                    previousParticle = enxame._particulas[idx - 1]
                else:
                    nextParticle = enxame._particulas[idx + 1]
                    previousParticle = enxame._particulas[idx - 1]
                vizinhanca.append(VizinhancaModel([previousParticle, curParticle, nextParticle]))
            return vizinhanca

    def updateVizinhancaMelhorPosicao(self, model):
        for curParticle in model._particulas:
            if model._melhorPosicaoFitness is None or (curParticle._fitness < model._melhorPosicaoFitness and curParticle._fitness is not None):
                model._melhorPosicaoFitness = curParticle._fitness
                model._melhorPosicao = np.copy(curParticle._melhorPosicao)

        for curParticle in model._particulas:
            curParticle._nbBestPosition = np.copy(model._melhorPosicao)