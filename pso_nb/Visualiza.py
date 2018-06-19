import numpy as np
import matplotlib.pyplot as plt

class Visualiza:

    particula = None
    EIXO_X    = []
    EIXO_Y    = []
    tamX      = None
    tamY      = None 

    # def __init__(self):
    #     # self.particula = np.random.randint(2, size = 59)
    #     # self.particula = particula
    #     self.EIXO_X 

    def ponto(self, particula):
        eX, eY, tamX, tamY = self.eixo(particula)
        self.EIXO_X.append[eX]
        self.EIXO_Y.append[eY]

    def show(self):
        plt.plot(self.EIXO_X, self.EIXO_Y, 'ro')
        plt.axis([0, pow(2, self.tamX), 0, pow(2, self.tamY)])
        plt.show()

    def tamanho(self, particula):
        x = (int)(particula.size/2)
        eixo_x = particula[0:x]
        eixo_y = particula[x:particula.size]
        self.tamX = eixo_x.size
        self.tamY = eixo_y.size

    def eixo(self, particula):
        x = (int)(particula.size/2)
        eixo_x = particula[0:x]
        eixo_y = particula[x:particula.size]
        
        eixo = ""
        for bit in eixo_x:
            eixo = eixo+str(bit)
        eX = int(eixo, base=2)
        
        eixo = ""
        for bit in eixo_y:
            eixo = eixo+str(bit)
        eY = int(eixo, base=2)

        return eX, eY

