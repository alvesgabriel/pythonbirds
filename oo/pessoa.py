class Pessoa:
    def __init__(self, *filhos, nome=None, idade=28):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

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
    gabriel.sobrenome = 'Alves'
    print(gabriel.sobrenome)
    del gabriel.filhos
    print(gabriel.__dict__)
    print(laura.__dict__)