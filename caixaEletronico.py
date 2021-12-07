saque = float(input("Digite o valor do saque, mínimo $10, máximo $600: "))
notas100 = 0
notas50 = 0
notas10 = 0
notas5 = 0
notas1 = 0

if(saque < 10 or saque > 600):
    print("Valor inválido!")
else:
    while saque > 0:
        if(saque >= 100):
            saque = saque - 100
            notas100 += 1
        elif(saque >= 50):
            saque = saque - 50
            notas50 += 1
        elif(saque >= 10):
            saque = saque -10
            notas10 +=1
        elif(saque >= 5):
            saque = saque - 5
            notas5 += 1
        elif(saque >= 1):
            saque = saque - 1
            notas1 +=1

print("Notas de 100: ", notas100, "Notas de 50: ", notas50, "Notas de 10: ", notas10, "Notas de 5: ", notas5, "Notas de 1: ", notas1)