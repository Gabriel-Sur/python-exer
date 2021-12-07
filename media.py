nota1 = float(input("Informe a nota 1: "))
nota2 = float(input("Informe a nota 2: "))

media = (nota1 + nota2) / 2

if(media >= 9.0 and media < 10.0):
    print("Nota 1: ", nota1, "Nota 2: ", nota2, "Média: ", media, "Conceito: A  Aprovado!")
elif(media >= 7.5 and media < 9.0):
    print("Nota 1: ", nota1, "Nota 2: ", nota2, "Média: ", media, "Conceito: B  Aprovado!")
elif(media >= 6.0 and media < 7.5):
    print("Nota 1: ", nota1, "Nota 2: ", nota2, "Média: ", media, "Conceito: C  Aprovado!")
elif(media >= 4.0 and media < 6.0):
    print("Nota 1: ", nota1, "Nota 2: ", nota2, "Média: ", media, "Conceito: D  Reprovado!")
else:
    print("Nota 1: ", nota1, "Nota 2: ", nota2, "Média: ", media, "Conceito: E  Reprovado!")