from datetime import date

data1 = float(input("digite seu ano de nascimento: "))
data2 = date.today().year
idade = data2-data1
if idade >= 18:
    print("Você é maior de idade. Sua idade é:", idade, "anos")
else:
    print("Você é menor de idade. Sua idade é:", idade, "anos")


salario = float(input("Informe o seu salário: "))
despesas = float(input("Informe o total de suas despesas: "))

saldo = salario - despesas

print("Seu saldo restante é: R$", saldo)