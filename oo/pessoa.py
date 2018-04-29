class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    laura = Pessoa(nome='Laura')
    gabriel = Pessoa(laura, nome='Gabriel')
    print(Pessoa.cumprimentar(gabriel))
    print(id(gabriel))
    print(gabriel.cumprimentar())
    print(gabriel.nome)
    print(gabriel.idade)
    for filho in gabriel.filhos:
        print(filho.nome)
    gabriel.olhos = 4
    gabriel.sobrenome = 'Alves'
    print(gabriel.sobrenome)
    del gabriel.filhos
    print(gabriel.__dict__)
    print(laura.__dict__)
    print(Pessoa.olhos)
    print(gabriel.olhos)
    print(laura.olhos)
    print(id(Pessoa.olhos), id(gabriel.olhos), id(laura.olhos))
    print(Pessoa.metodo_estatico(), gabriel.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), gabriel.nome_e_atributo_de_classe())