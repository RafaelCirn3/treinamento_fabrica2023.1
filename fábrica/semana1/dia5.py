string = input("Digite uma frase: ")
letras = 0
for char in string:
    if char.isalpha():
        letras += 1
print("Número de letras na frase:", letras)

def verifica_palavra(string, palavra):

    if palavra in string:
        return True
    else:
        return False
string_exemplo = "bananas são frutas "
print(string_exemplo)
palavra_exemplo = input("Digite a palavra a ser procurada na string: ")

resultado = verifica_palavra(string_exemplo, palavra_exemplo)
print(resultado)