print("Responda com 'Sim' ou 'Não'.")
a = str(input("Telefonou para a vítima? "))

respostas = 0

if(a == "Sim" or a == "sim"):
    respostas += 1
elif(a == "Não" or a == "não" or a == "nao"):
    respostas += 0
else:
    print("Resposta inválida!")                                #TENTEI APLICAR A FUNÇÃO DEF PARA NÃO DEIXAR O CÓDIGO VERBOSO MAS NÃO DEU CERTO :(

b = str(input("Esteve no local do crime? "))

if(b == "Sim" or b == "sim"):
    respostas += 1
elif(b == "Não" or b == "não" or b == "nao"):
    respostas += 0
else:
    print("Resposta inválida!")

c = str(input("Mora perto da vítima? "))
if(c == "Sim" or c == "sim"):
    respostas += 1
elif(c == "Não" or c == "não" or c == "nao"):
    respostas += 0
else:
    print("Resposta inválida!")

d = str(input("Devia para a vítima? "))
if(d == "Sim" or d == "sim"):
    respostas += 1
elif(d == "Não" or d == "não" or d == "nao"):
    respostas += 0
else:
    print("Resposta inválida!")

e = str(input("Já trabalhou com a vítima? "))
if(e == "Sim" or e == "sim"):
    respostas += 1
elif(e == "Não" or e == "não" or e == "nao"):
    respostas += 0
else:
    print("Resposta inválida!")

if(respostas == 2):
    print("Suspeito!")
elif(respostas == 3 or respostas == 4):
    print("Cúmplice!")
elif(respostas == 5):
    print("Assasino!")
else:
    print("Inocente")

