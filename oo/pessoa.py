class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'Olá {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    iury = Pessoa(nome ='Iury')
    ana = Pessoa( nome = 'Ana')
    artur = Pessoa(ana,iury, nome ='Artur')
    
    print(Pessoa.comprimentar(iury))
    print(id(iury))
    print(iury.comprimentar())
    print(iury.nome)
    for filho in artur.filhos:
        print(filho.nome)
    iury.olhos = 1
    print(artur.__dict__)
    print(iury.__dict__)
    
    print(Pessoa.olhos)
    print(iury.olhos)
    print(artur.olhos)
    print(id(Pessoa.olhos), id(iury.olhos),id(artur.olhos))
    print(Pessoa.metodo_estatico(), iury.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), iury.nome_e_atributos_de_classe())