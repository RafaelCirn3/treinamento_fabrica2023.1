pessoas = []
pessoa_mais_pesada = pessoa_mais_leve = None

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break

    peso = float(input("Digite o peso da pessoa: "))

    pessoa = (nome, peso)
    pessoas.append(pessoa)

    if not pessoa_mais_pesada or peso > pessoa_mais_pesada[1]:
        pessoa_mais_pesada = pessoa

    if not pessoa_mais_leve or peso < pessoa_mais_leve[1]:
        pessoa_mais_leve = pessoa

quantidade_pessoas = len(pessoas)

print(f"Quantidade de pessoas cadastradas: {quantidade_pessoas}")

if pessoa_mais_pesada:
    print(f"Pessoa mais pesada: {pessoa_mais_pesada[0]}, peso: {pessoa_mais_pesada[1]}")
else:
    print("Nenhuma pessoa cadastrada.")

if pessoa_mais_leve:
    print(f"Pessoa mais leve: {pessoa_mais_leve[0]}, peso: {pessoa_mais_leve[1]}")
else:
    print("Nenhuma pessoa cadastrada.")

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    aluno = [nome, nota1, nota2]
    alunos.append(aluno)

print("\nBoletim:")

for aluno in alunos:
    nome = aluno[0]
    media = sum(aluno[1:]) / len(aluno[1:])
    print(f"\nNome: {nome}")
    print(f"Média: {media:.2f}")

while True:
    opcao = input("\nDigite o nome de um aluno para ver as notas (ou 'sair' para encerrar): ")

    if opcao.lower() == 'sair':
        break

    encontrado = False

    for aluno in alunos:
        if aluno[0].lower() == opcao.lower():
            encontrado = True
            notas = aluno[1:]
            print(f"\nNotas de {aluno[0]}: {notas}")

    if not encontrado:
        print("Aluno não encontrado.")
