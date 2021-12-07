dia = str(input("Digite o dia: "))
mes = str(input("Digite o mês: "))
ano = str(input("Digite o ano: "))

validar = 0

if(dia.__len__() == 2 and 31 >= int(dia)):
    validar += 1
if(mes.__len__() == 2 and 12 >= int(mes)):
    validar += 1
if(ano.__len__() == 4 and 2020 >= int(ano)):
    validar +=1

if(validar == 3):
    print("Data válida!")
else:
    print("Data inválida!")


