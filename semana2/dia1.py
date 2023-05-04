valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos você pretende pagar: "))

prestacao = valor_casa / (anos * 12)
limite_prestacao = salario * 0.3

if prestacao > limite_prestacao:
    print("Empréstimo negado.")
else:
    print(
        f"Empréstimo aprovado. Valor da prestação mensal: R$ {prestacao:.2f}")





preco = float(input("Digite o preço do produto: "))
pagamento = int(input("Digite a forma de pagamento (1-à vista dinheiro/pix, 2-à vista no cartão, 3-em até 2x no cartão, 4-3x ou mais no cartão): "))

if pagamento == 1:
    preco_final = preco * 0.9
elif pagamento == 2:
    preco_final = preco * 0.95
elif pagamento == 3:
    preco_final = preco
elif pagamento == 4:
    preco_final = preco * 1.2
else:
    print("Forma de pagamento inválida.")
    preco_final = preco

print(f"Preço final do produto: R$ {preco_final:.2f}")
