morango = float(input("Quantos kilos de morango você deseja? "))

maca = float(input("Quantos kilos de maçâ você deseja? "))

if(morango <= 5 ):
    precomorango = morango * 2.50
else:
    precomorango = morango * 2.20

if(maca <= 5 ):
    precomaca = maca * 1.80
else:
    precomaca = maca * 1.50

if(morango > 8 or precomorango >= 25.00):
    precomorango = precomorango * 0.9

if(maca > 8 or precomaca >= 25.00):
    precomaca = precomaca * 0.9

print("Preço do morango: ", precomorango, "Preço da maçâ: ", precomaca)