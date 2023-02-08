#criar três classes com pelo menos dois atributos e dois metodos cada:
from Classes import Campeoes

nome = input("digite o nome do campeao: ")
dano = input("digite o tipo de dano: ")

campeao = Campeoes(nome, dano)
tipo = "none"

if (campeao.dano == "ap"):
  tipo = "maguinho lixeira"
elif(campeao.dano == "ad"):
  tipo = "assassino imundo"
else:
  print("campeão desconhecido.")



print(tipo)