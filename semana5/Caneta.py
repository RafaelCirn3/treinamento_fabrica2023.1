class Caneta:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

    def ler_caneta(self):
        return f'a cor da minha caneta é { self.cor }e sua marca é {self.marca}'
        # self.__cor = self.set_cor(cor)
        # self.__marca = marca

    # def get_cor(self):
    #     return self.__cor

    # def set_cor(self, cor):
    #     if isinstance(cor, str):
    #         self.__cor = cor
    #     else:
    #         self.__cor = None
