import os
from funcoes import menu
from funcoes import jogar
palavra_escondida = []
letras_descobertas = []
errou = True
vida = 5
vencedor = ""
perdedor = ""


print("\n *** Jogo da Forca *** \n")

nomeD = input("Digite o nome do desafiante: ")

nomeC = input("Digite o nome do competidor: ")


os.system('cls')

palavra = str.lower(input("Desafiante, digite a palavra chave: "))
palavra_array = [0]*len(palavra)
dica1 = input("Digite a dica 1: ")
dica2 = input("Digite a dica 2: ")
dica3 = input("Digite a dica 3: ")
os.system('cls')

print("A palavra chave possui ", len(palavra), "letras.")
for i in range(0, len(palavra)):
    letras_descobertas.append("*")
print(letras_descobertas)

dicas = 3
   
menu()

acertou = False

jogar()

historico = open("historico.txt","w")
historico.write("\nPalavra: ", palavra, "Vencedor: ", vencedor, "Perdedor: ", perdedor)
historico.close()