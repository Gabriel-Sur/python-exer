x = float(input("Informe o preço do primeiro produto: "))
y = float(input("Informe o preço do segundo produto:"))
z = float(input("Informe o preço do terceiro produto"))

if(x < z and x < y):
    print("Você deve comprar o primeiro produto.")
elif(z < x and z < y):
    print("Você deve comprar o terceiro produto.")
else:
    print("Você deve comprar o segundo produto.")