"""
deve criar uma classe carro que vai possuir dois atributos
compostos por outras duas classes:

1) motor
2) direção

O motor terá a responsabilidade de controlar a velocidade.
ele oferece os seguintes atributos:
1) atributo de dado velocidade
2) metodo acelerar, quer deverar incremetar a velocidade de uma unidade
3) metodo frear que devera decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção.
Ela oderece os seguintes atributos:
1) valor de direção com valores possíveis: norte, sul, leste, oeste
2) metodo girar a direita e esquerda
    N
  O   L
    s

    Exemplo:
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'


"""


class Motor:

    def __init__(self, ):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        # if self.velocidade == 0 or self.velocidade == 1:
        #     self.velocidade = 0
        # else:
        #     self.velocidade -= 2
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE,
        LESTE: SUL,
        SUL: OESTE,
        OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE,
        LESTE: NORTE,
        SUL: LESTE,
        OESTE: SUL
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        # if self.valor == NORTE:
        #     self.valor = LESTE
        # elif self.valor == LESTE:
        #     self.valor = SUL
        # elif self.valor == SUL:
        #     self.valor = OESTE
        # else:
        #     self.valor = NORTE
        """EM CASO DE IF E ELIF, DA PRA SE USAR DICIONARIO"""
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        # if self.valor == NORTE:
        #     self.valor = OESTE
        # elif self.valor == LESTE:
        #     self.valor = NORTE
        # elif self.valor == SUL:
        #     self.valor = LESTE
        # else:
        #     self.valor = SUL
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
