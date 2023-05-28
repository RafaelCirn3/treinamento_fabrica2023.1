from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, funcionario):
        super().__init__(nome, salario)
        self.funcionario = funcionario
    
    def emitir_aumento(self)
    