class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def comprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def comprimentar(self):
        comprimentar_da_casse= super().comprimentar()
        return f'{comprimentar_da_casse} - Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    iury = Mutante(nome ='Iury')
    ana = Pessoa( nome = 'Ana')
    artur = Homem(nome ='Artur')
    
    print(Pessoa.comprimentar(iury))
    print(id(iury))
    print(iury.comprimentar())
    print(iury.nome)
    for filho in artur.filhos:
        print(filho.nome)
    print(artur.__dict__)
    print(iury.__dict__)
    
    print(Pessoa.olhos)
    print(iury.olhos)
    print(artur.olhos)
    print(id(Pessoa.olhos), id(iury.olhos),id(artur.olhos))
    print(Pessoa.metodo_estatico(), iury.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), iury.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(iury, Pessoa))
    print(iury.olhos)
    print(iury.comprimentar())
    print(artur.comprimentar())
