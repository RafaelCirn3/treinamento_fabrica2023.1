numeros = []
pares = []
impares = []

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista completa de números:", numeros)
print("Lista de números pares:", pares)
print("Lista de números ímpares:", impares)


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
