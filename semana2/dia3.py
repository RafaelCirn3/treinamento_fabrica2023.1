# maior = 0
# menor = 0
# for p in range(1, 6):
#     peso = float(input('Peso da {}ª pessoa: '.format(p)))
#     if p == 1: 
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso

# print('O maior peso lido foi de {}Kg'.format(maior))
# print('O menor peso lido foi de {}Kg'.format(menor))

soma = 0
cont_mulheres = 0
media = 0
maior = 0
nomeHomemMais_Velho = ''


for cont in range(1,5):

    nome = input('Digite o seu nome: ')
    sexo = input('Masculino ou Feminino ? [M/F]').upper()[0]
    idade = int(input('Digite a sua idade : '))
    print('-'*20)

    soma = soma + idade 
    media = soma / cont 

    if sexo == 'M' and idade > maior:
        maior = idade
        nomeHomemMais_Velho = nome

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

print('Media das idades é de {:.2f} '.format(media))
print('Nome do mais velho é {}'.format(nomeHomemMais_Velho))

if cont_mulheres == 0:
    print('Não temos mulheres no grupo !')

else:
    print('A todo temos {} mulheres com menor de 20 anos'.format(cont_mulheres))