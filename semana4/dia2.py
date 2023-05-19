
def contador(inicio, fim, passo):
    if passo == 0:
        print("Erro: O valor do passo não pode ser zero.")
        return

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    
    print()


# Contagem de 1 até 10, de 1 em 1
print("Contagem de 1 até 10, de 1 em 1:")
contador(1, 10, 1)

# Contagem de 10 até 0, de 2 em 2
print("Contagem de 10 até 0, de 2 em 2:")
contador(10, 0, 2)

# Contagem personalizada
print("Contagem personalizada:")
contador(5, 20, 3)
