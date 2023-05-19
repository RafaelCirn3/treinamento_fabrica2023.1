valores = []

while True:
    valor = int(input("Digite um valor (ou 0 para sair): "))

    if valor == 0:
        break

    if valor not in valores:
        valores.append(valor)

valores.sort()

print("Valores únicos digitados, em ordem crescente:")
for valor in valores:
    print(valor)


numeros = []

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    numeros.append(numero)

quantidade_numeros = len(numeros)
numeros_decrescente = sorted(numeros, reverse=True)
valor_5_presente = 5 in numeros

print(f"Quantidade de números digitados: {quantidade_numeros}")
print("Lista de valores em ordem decrescente:")
for numero in numeros_decrescente:
    print(numero)

if valor_5_presente:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não está na lista.")
