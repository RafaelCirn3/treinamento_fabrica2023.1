import random
from datetime import date

print("Jogo de Pedra, Papel e Tesoura")
opcoes = ["Pedra", "Papel", "Tesoura"]
while True:
    escolha_usuario = input(
        "Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ")
    escolha_usuario = escolha_usuario
    if escolha_usuario == "Sair":
        break

    if escolha_usuario not in opcoes:
        print("Opção inválida. Tente novamente.")
        continue

    escolha_pc = random.choice(opcoes)
    print(
        f"Você escolheu {escolha_usuario}. O computador escolheu {escolha_pc}.")
    if escolha_usuario == escolha_pc:
        print("Empatou")
    elif escolha_usuario == "Pedra" and escolha_pc == "Tesoura" or \
            escolha_usuario == "Papel" and escolha_pc == "Pedra" or \
            escolha_usuario == "Tesoura" and escolha_pc == "Papel":
        print("Você ganhou")
    else:
        print("O sistema ganhou")


ano_atual = date.today().year
maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"{maiores} pessoas são maiores de idade e {menores} pessoas ainda são menores de idade.")
