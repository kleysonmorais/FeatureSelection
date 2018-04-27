from Models import *
from FeatureSelection.cfs import cfs

import numpy as np

class ParticulaController:

    def criarParticular(self, particula, nAtributos):
        #Criar array com posição (binário)
        particula._posicao = np.random.randint(2, size = nAtributos)
        #Criar array com velocidade (binário)
        particula._velocidade = np.random.randint(2, size = nAtributos)
        #Melhor posição já passada iniciar com a primeira posição
        particula._melhorPosicaoLocal = particula._posicao
        #Salvar o fitness da respectiva posição
        self.atualizaFitness(particula)

    def atualizaFitness(self, particula):
        #Função para calcular o fitness da partícula
        # merito = cfs (particula._posicao)
        if particula._fitness is None or merito < particula._fitness:
            particula._melhorPosicaoLocal = np.copy(particula._posicao)
            particula._fitness = merito

    def atualizaPosicao(self, particula):
        c = 2.5
        e1 = np.random.rand() #Verificar
        e2 = np.random.rand() 
        valorMaximo = 6
        for i, velocidade in enumerate(particula._velocidade):
            velocidade = velocidade + c * e1 * (particula._melhorPosicaoLocal[i] - particula._posicao[i]) + c * e2 * (model._melhorPosicaoGlobal[i] - model._posicao[i])
            #Verificar Limite
            if abs(velocidade) > valorMaximo and abs(velocidade) is velocidade:
                velocidade = valorMaximo
            elif abs(velocidade) > valorMaximo:
                velocidade = -valorMaximo
            velocidade = self.sigmoid(velocidade)
            if np.random.rand(1) < velocidade:
                model._posicao[i] = 1
            else:            
                model._posicao[i] = 0
        
    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-(x)))


class EnxameController:

    pc = None

    def __init__(self):
        self.pc = ParticulaController()

    def criarEnxame(self, enxame, nParticulas, nAtributos):
        for i in range(nParticulas):
            #Criando instância de uma nova partícula e adicionando ao enxame
            novaParticula = ParticulaModel()
            self.pc.criarParticular(novaParticula, nAtributos)
            enxame._particulas.append(novaParticula)
        
        self.atualizaMelhorPosicaoEnxame(enxame)
        
    def atualizaMelhorPosicaoEnxame(self, enxame):
        for particula in enxame._particulas:
            if (enxame._melhorPosicaoGlobal is None and enxame._melhorFitness is None) or (particula._fitness < enxame._melhorFitness):
                enxame._melhorPosicaoGlobal = np.copy(particula._melhorPosicaoLocal)
                enxame._melhorFitness = particula._melhorFitness
            
        for particula in enxame._particulas:
            particula._melhorPosicaoGlobal = np.copy(enxame._melhorPosicaoGlobal)

    def atualizaEnxame(self, enxame):
        for particula in enxame._particulas:
            self.pc.atualizaPosicao(particula)
            self.pc.atualizaFitness(particula)
        self.atualizaMelhorPosicaoEnxame(enxame)
