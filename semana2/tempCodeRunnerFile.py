print("Jogo de Pedra, Papel e Tesoura")
# opcoes = ["Pedra", "Papel", "Tesoura"]
# while True:
#     escolha_usuario = input(
#         "Escolha Pedra, Papel ou Tesoura (ou 'sair' para encerrar): ")
#     escolha_usuario = escolha_usuario
#     if escolha_usuario == "Sair":
#         break

#     if escolha_usuario not in opcoes:
#         print("Opção inválida. Tente novamente.")
#         continue

#     escolha_pc = random.choice(opcoes)
#     print(
#         f"Você escolheu {escolha_usuario}. O computador escolheu {escolha_pc}.")
#     if escolha_usuario == escolha_pc:
#         print("Empatou")
#     elif escolha_usuario == "Pedra" and escolha_pc == "Tesoura" or \
#             escolha_usuario == "Papel" and escolha_pc == "Pedra" or \
#             escolha_usuario == "Tesoura" and escolha_pc == "Papel":
#         print("Você ganhou")
#     else:
#         print("O sistema ganhou")