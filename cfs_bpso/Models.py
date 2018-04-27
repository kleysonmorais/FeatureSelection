#---- Representação da Partícula
class ParticulaModel:
    _posicao           = None
    _velocidade        = None
    _melhorPosicao     = None
    _melhorPosicaoPas  = None
    _fitness           = None

    def __init__(self):
        self._posicao           = None
        self._velocidade        = None
        self._melhorPosicao     = None
        self._melhorPosicaoPas  = None
        self._fitness           = None

#---- Representação do Enxame
class EnxameModel:
    _particulas              = None
    _vizinhanca              = None
    _melhorPosicao           = None
    _melhorPosicaoFitness    = None
    
    def __init__(self):
        self._particulas = []
        self._vizinhanca             = None
        self._melhorPosicao          = None
        self._melhorPosicaoFitness   = None

#---- Representação da Vizinhança    
class VizinhancaModel:
    _particulas              = []
    _melhorPosicao           = None
    _melhorPosicaoFitness    = None
    
    def __init__(self, particulas):
        self._particulas             = particulas
        self._melhorPosicao          = None
        self._melhorPosicaoFitness   = None