import random


def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 10))
    return numeros


def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma


# Sortear 5 números
numeros_sorteados = sorteia()
print("Números sorteados:", numeros_sorteados)

# Calcular a soma dos valores pares
soma_valores_pares = somaPar(numeros_sorteados)
print("Soma dos valores pares:", soma_valores_pares)
