from personagem import Personagem
from arma import Arma

minha_arma = Arma("Lâmina Oculta", "Lâmina")
meu_personagem= Personagem("Ezio", "Assassin", minha_arma)

print(f"Nome do Personagem: {meu_personagem.nome}")
print(f"Classe do Personagem: {meu_personagem.classe}")
print(f"Nome da Arma: {meu_personagem.arma.nome}")
print(f"Tipo da Arma: {meu_personagem.arma.tipo}")
