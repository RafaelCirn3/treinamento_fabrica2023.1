frase = input("Digite uma frase: ")
frase_sem_espaco = frase.replace(" ", "")
num_caracteres = len(frase_sem_espaco)
print("Frase:", frase)
print("Número de caracteres (sem espaço):", num_caracteres)

exemplo = "treinamento hoje de backend"
print("Frase original:", exemplo)

palavra_antiga = input("Digite a palavra que você deseja substituir: ")
palavra_nova = input("Digite a nova palavra: ")

nova_frase = exemplo.replace(palavra_antiga, palavra_nova)
print("Nova frase:", nova_frase)
