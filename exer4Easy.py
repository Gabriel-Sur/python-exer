dia = 0
mes = 0 
ano = 0

dias = int(input("Digite sua idade em dias: "))

while dias > 0:
    if(dias >= 365):
        dias = dias - 365
        ano += 1
    elif(dias >= 30 and mes < 11):
        dias = dias - 30
        mes = mes + 1
    else:
        dia = dias
        dias = 0


print(ano, "ano(s)")
print(mes, "mes(es)")
print(dia, "dia(s)")
        
        

