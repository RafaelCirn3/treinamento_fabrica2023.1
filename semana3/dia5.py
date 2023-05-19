jogador = {}

jogador["nome"] = input("Digite o nome do jogador: ")
quantidade_partidas = int(input("Digite a quantidade de partidas jogadas: "))

gols_por_partida = []
total_gols = 0

for partida in range(1, quantidade_partidas + 1):
    gols = int(input(f"Digite a quantidade de gols feitos na partida {partida}: "))
    gols_por_partida.append(gols)
    total_gols += gols

jogador["gols_por_partida"] = gols_por_partida
jogador["total_gols"] = total_gols

print("\nDados do jogador:")
print("Nome:", jogador["nome"])
print("Gols por partida:", jogador["gols_por_partida"])
print("Total de gols:", jogador["total_gols"])


from datetime import date

dados_pessoa = {}

dados_pessoa["nome"] = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
dados_pessoa["idade"] = date.today().year - ano_nascimento
dados_pessoa["ctps"] = int(input("Digite o número da carteira de trabalho (0 se não tiver): "))

if dados_pessoa["ctps"] != 0:
    dados_pessoa["ano_contratacao"] = int(input("Digite o ano de contratação: "))
    dados_pessoa["salario"] = float(input("Digite o salário: "))

    idade_aposentadoria_homens = 65
    idade_aposentadoria_mulheres = 62

    if dados_pessoa["ctps"] != 0:
        if dados_pessoa["ano_contratacao"] + idade_aposentadoria_homens - ano_nascimento <= date.today().year:
            dados_pessoa["idade_aposentadoria"] = idade_aposentadoria_homens
        else:
            dados_pessoa["idade_aposentadoria"] = idade_aposentadoria_homens + 1
    else:
        if dados_pessoa["ano_contratacao"] + idade_aposentadoria_mulheres - ano_nascimento <= date.today().year:
            dados_pessoa["idade_aposentadoria"] = idade_aposentadoria_mulheres
        else:
            dados_pessoa["idade_aposentadoria"] = idade_aposentadoria_mulheres + 1

print("\nDados da pessoa:")
print("Nome:", dados_pessoa["nome"])
print("Idade:", dados_pessoa["idade"])
print("CTPS:", dados_pessoa["ctps"])

if dados_pessoa["ctps"] != 0:
    print("Ano de contratação:", dados_pessoa["ano_contratacao"])
    print("Salário:", dados_pessoa["salario"])
    print("Idade de aposentadoria:", dados_pessoa["idade_aposentadoria"])
