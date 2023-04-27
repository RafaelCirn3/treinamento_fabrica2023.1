# numero1 = float(input("Digite o primeiro número inteiro: "))
# numero2 = float(input("Digite o segundo número inteiro: "))
# numero3 = float(input("Digite o terceiro número inteiro: "))

# if numero1 == numero2 and numero1 == numero3:
#     print("Três iguais")
# elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
#     print("Dois iguais")
# else:
#     print("Três diferentes")

num1 = float(input("digite um número: "))
num2 = float(input("digite um número: "))
num3 = float(input("digite um número: "))
num4 = float(input("digite um número: "))
num5 = float(input("digite um número: "))

maior_numero = num1

if num2 > maior_numero:
    maior_numero = num2
elif num3 > maior_numero:
    maior_numero = num3
elif num4 > maior_numero:
    maior_numero = num4
if num5 > maior_numero:
    maior_numero = num5
print("O maior número é: ", maior_numero)
