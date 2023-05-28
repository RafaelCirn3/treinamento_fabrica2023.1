class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def mostrar_dados(self):
        return f'meu nome é {self.nome}, tenho {self.idade} anos de idade e {self.altura} m de altura'
