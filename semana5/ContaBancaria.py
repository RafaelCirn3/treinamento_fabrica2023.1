class ContaBancaria:
    def __init__(self, nome, numaccount, saldo = 0):
        self.nome = nome
        self.numaccount = numaccount
        self.saldo = saldo
    

    def depositar(self, valor):
        self.saldo += valor
    print(f'deposito realizado. novo saldo: ', self.saldo)

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque realizado. Novo saldo:", self.saldo)