class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
