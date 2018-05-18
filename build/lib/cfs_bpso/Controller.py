#------------------------------------------------------------------------------+
#
#   Morais, Kleyson.
#   April, 2018
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from Models import *
from cfs import cfs
from benchmark.avaliador import AvaliadorController
import numpy as np

class ParticulaController:

    dadosModel = None
    nome_base_dados = None
    tipo = None
    ac = None

    def __init__(self, nome, tipo="filtro"):
        self.nome_base_dados = nome
        self.tipo = tipo

    def __init__(self, avaliador, tipo):
        self.ac = avaliador
        self.tipo = tipo

    def criarParticular(self, particula, dados):
        '''
        Esta função cria uma partícula para o enxame, personalizando a mesma para que tenha as características 
        do banco de dados informado.

        - São gerados aleatoriamente: Posição e Velociade
        - Cada partícula possui também a melhor posição pela qual ela já passou e seu respectivo fitness
        '''
        self.dadosModel = dados
        nLinhas, nAtributos = self.dadosModel._dados.shape
        #Criar array com posição (binário)
        particula._posicao = np.random.randint(2, size = nAtributos)
        #Criar array com velocidade (binário)
        particula._velocidade = np.random.randint(2, size = nAtributos)
        #Melhor posição já passada iniciar com a primeira posição
        particula._melhorPosicaoLocal = particula._posicao
        #Salvar o fitness da respectiva posição
        self.atualizaFitness(particula)
        print("Partícula Criada:")
        print(particula._posicao,' | ', particula._fitness)

    def atualizaFitness(self, particula):
        '''
        Função para calcular o fitness da partícula, onde 1 significa atributo utilizado e 0 não utilizado
        '''
        #O condicional a seguir seleciona um subgrupo de atributos selecionados
        if self.tipo == "filtro":
            aux = np.asarray(self.dadosModel._dados)
            if np.count_nonzero(particula._posicao) == 0:
                X_subset = aux
            else:
                X_subset = aux[:,particula._posicao==1]

            #Chamada do cálculo do mérito utilizando o subconjunto escolhido
            #Usando Seleção Baseada em Correlação (CFS)
            merito = cfs.meritoBuffer(X_subset, self.dadosModel._atributoClassificador, particula._posicao, self.nome_base_dados)
            if particula._fitness is None or merito < particula._fitness:
                particula._melhorPosicaoLocal = np.copy(particula._posicao)
                particula._fitness = merito
        else:
            merito = self.ac.NaiveBayes(particula._posicao)
            if particula._fitness is None or merito > particula._fitness:
                particula._melhorPosicaoLocal = np.copy(particula._posicao)
                particula._fitness = merito

    def atualizaPosicao(self, particula):
        '''
        Esta função é responsável pela movimentação das partículas no espaço, calculando suas respectivas velocidades
        para descobrir as novas posições.

        - A variáveis c é constante para o cálculo, convencionalmente utiliza-se 2.5
        - e1 e e2 são variáveis de atrito para o movimento da partícula
        - valorMaximo é um limite que não permite a ser ultrapassada, convencionalmente utiliza-se [-6, 6]
        '''
        c = 2.5
        #Número aleatório entre 0 e 1
        e1 = np.random.rand() 
        e2 = np.random.rand() 
        valorMaximo = 6
        for i, velocidade in enumerate(particula._velocidade):
            #Calculando velocidade
            velocidade = velocidade + c * e1 * (particula._melhorPosicaoLocal[i] - particula._posicao[i]) + c * e2 * (particula._melhorPosicaoGlobal[i] - particula._posicao[i])
            #Verificar Limite
            if abs(velocidade) > valorMaximo and abs(velocidade) is velocidade:
                velocidade = valorMaximo
            elif abs(velocidade) > valorMaximo:
                velocidade = -valorMaximo
            velocidade = self.sigmoid(velocidade)
            #Condicional de definição 0 ou 1
            if np.random.rand(1) < velocidade:
                particula._posicao[i] = 1
            else:            
                particula._posicao[i] = 0
        
    def sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-(x)))


class EnxameController:

    pc              = None
    dadosModel      = None
    tipo            = None

    def __init__(self, DadosModel, nome):
        self.pc = ParticulaController(nome)
        self.dadosModel = DadosModel
    
    def __init__(self, DadosModel, avaliador, tipo):
        self.pc = ParticulaController(avaliador=avaliador, tipo=tipo)
        self.dadosModel = DadosModel
        self.tipo = tipo

    def criarEnxame(self, enxame, nParticulas):
        print("Criando Enxame de Partículas")
        for i in range(nParticulas):
            #Criando instância de uma nova partícula e adicionando ao enxame
            novaParticula = ParticulaModel()
            self.pc.criarParticular(novaParticula, self.dadosModel)
            enxame._particulas.append(novaParticula)
        
        self.atualizaMelhorPosicaoEnxame(enxame)
        
    def atualizaMelhorPosicaoEnxame(self, enxame):
        print("Atualizando Melhor Posição do Enxame")
        if self.tipo == "filtro":
            for particula in enxame._particulas:
                if (enxame._melhorFitness is None) or (particula._fitness < enxame._melhorFitness):
                    enxame._melhorPosicaoGlobal = np.copy(particula._melhorPosicaoLocal)
                    enxame._melhorFitness = particula._fitness
        else:
            for particula in enxame._particulas:
                if (enxame._melhorFitness is None) or (particula._fitness > enxame._melhorFitness):
                    enxame._melhorPosicaoGlobal = np.copy(particula._melhorPosicaoLocal)
                    enxame._melhorFitness = particula._fitness    
            
        print("Partícula com a Melhor Posição Global: ")
        print(enxame._melhorPosicaoGlobal, ' | ', enxame._melhorFitness)

        for particula in enxame._particulas:
            particula._melhorPosicaoGlobal = np.copy(enxame._melhorPosicaoGlobal)

    def atualizaEnxame(self, enxame):
        for particula in enxame._particulas:
            self.pc.atualizaPosicao(particula)
            self.pc.atualizaFitness(particula)
        self.atualizaMelhorPosicaoEnxame(enxame)
