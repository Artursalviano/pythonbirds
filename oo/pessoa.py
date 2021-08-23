class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    iury = Pessoa(nome ='Iury')
    artur = Pessoa(iury, nome ='Artur')
    ana = Pessoa( nome = 'Ana')
    print(Pessoa.comprimentar(iury))
    print(id(iury))
    print(iury.comprimentar())
    print(iury.nome)
    for filho in artur.filhos:
        print(filho.nome)

