class Pessoa:
    def cumprimentar(self):
        return print('Olá!')

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print()
    print(id(p))
    print()
    print(p.cumprimentar())
