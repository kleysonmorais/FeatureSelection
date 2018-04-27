# Representação da Partícula
class ParticulaModel:
    _posicao                 = None
    _velocidade              = None
    _melhorPosicaoLocal      = None
    _melhorPosicaoGlobal     = None
    _fitness                 = None

    def __init__(self):
        self._posicao               = None
        self._velocidade            = None
        self._melhorPosicaoLocal    = None
        self._melhorPosicaoGlobal   = None
        self._fitness               = None

# Representação do Enxame
class EnxameModel:
    _particulas                     = None
    _melhorPosicaoGlobal            = None
    _melhorFitness                  = None

    def __init__(self):
        self._particulas                  = []
        self._melhorPosicaoGlobal         = None
        self._melhorFitness               = None