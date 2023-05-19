def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")

# Exemplo de uso da função leiaInt()
n = leiaInt("Digite um número inteiro: ")
print("O número digitado foi:", n)
