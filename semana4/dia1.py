from time import sleep


def soma():
    x = float(input('digite um número:'))
    y = float(input('digite um número:'))
    print('soma =', x+y)


def subtracao():
    x = float(input('digite um número:'))
    y = float(input('digite um número:'))
    print('subtração', x-y)


def multiplicacao():
    x = float(input('digite um número:'))
    y = float(input('digite um número:'))
    print('multiplicação', x*y)


opcao = 1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    opcao = int(input("Opção: "))

    if (opcao == 1):
        soma()
    if (opcao == 2):
        subtracao()
    if (opcao == 3):
        multiplicacao()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)


def area(b, h):
    a = b * h
    print(f'A área de um terreno (b) . (h) é de um (a)m².')


b = float(input('comprimento m²: '))
h = float(input('altura m²: '))
a = b*h
print(a)


def maior(* num):
    cont = maior = 0
    print('--' * 30)
    print(' analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end='', flush=True)
        time.sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior
            maior = valor
        cont == 1
    print(f'foram informados {cont} valores ao todo')
    print(f' o maior valor informado foi {maior}.')


maior(8, 9, 3, 5, 2, 1)
maior(3, 8, 0)
maior(2, 7)
maior(5)
