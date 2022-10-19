class Pessoa:
    def __init__(self, nome=None, idade=48):
        self.nome = nome
        self.idade = idade


    def cumprimentar(self):
        return print('Olá!')


if __name__ == '__main__':
    p = Pessoa('Bolsonaro')
    print(Pessoa.cumprimentar(p))
    print()
    print(p.cumprimentar())
    print(id(p))
    print()
    p.nome = 'Adilson'
    print(p.nome)
    print(p.idade)