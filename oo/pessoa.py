class Pessoa:
    def __init__(self, *filhos, nome=None, idade=77):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá!{id(self)}'


if __name__ == '__main__':
    adilsonjr = Pessoa(nome='Adilson Jr')
    adilson_pai = Pessoa(adilsonjr, nome='Adilson Pai')
    Pessoa.cumprimentar(adilson_pai)
    print(id(adilson_pai))
    print(adilson_pai.cumprimentar())
    print(adilson_pai.nome)
    print(adilson_pai.idade)
    for filho in adilson_pai.filhos:
        print(filho.nome)
