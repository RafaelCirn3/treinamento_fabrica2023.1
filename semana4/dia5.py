def notar(*notas, situacao=False):
    quantidade = len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / quantidade

    resultado = {
        'quantidade': quantidade,
        'maior_nota': maior_nota,
        'menor_nota': menor_nota,
        'media': media
    }

    if situacao:
        if media >= 7:
            resultado['situacao'] = 'Aprovado'
        elif media >= 5:
            resultado['situacao'] = 'Recuperação'
        else:
            resultado['situacao'] = 'Reprovado'

    return resultado

# Exemplo de uso da função notar()
resultado = notar(7.5, 9.0, 6.5, 8.0, situacao=True)
print("Quantidade de notas:", resultado['quantidade'])
print("Maior nota:", resultado['maior_nota'])
print("Menor nota:", resultado['menor_nota'])
print("Média:", resultado['media'])
print("Situação:", resultado['situacao'])
