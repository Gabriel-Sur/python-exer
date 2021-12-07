
def menu(dicas,palavra, letras_descobertas, vida, dica1, dica2, dica3):
    while dicas > 0:
        menu = input("Digite 1 para Jogar ou 2 para Solicitar dica: ")
        if(menu == 1):
            letra = str.lower(input("Digite uma letra: "))
        
            for i in range(0, len(palavra)):
                if letra == palavra[i]:
                    letras_descobertas[i] = letra
                    errou = False

        
            print(letras_descobertas)
            for x in range(0, len(letras_descobertas)):
                if letras_descobertas[x] == "*":
                    acertou = False

            if errou == True:
                vida = vida -1
                print("Você errou! Você possui ", vida, "vidas.")

                if vida <= 0:
                    print("Suas vidas acabaram!")
                    
        else:
            if(dica1 == str):
                print(dica1)
                dica1 = 0
            elif(dica2 == str):
                print(dica2)
                dica2 = 0
            elif(dica3 == str):
                print(dica3)
                dica3 = 0
        
        dicas = dicas -1

def jogar(acertou, letra,palavra,letras_descobertas,vida, vencedor, perdedor):
    while acertou == False: 
        letra = str.lower(input("Digite uma letra: "))
        
        for i in range(0, len(palavra)):
            if letra == palavra[i]:
                letras_descobertas[i] = letra
                errou = False

        
        print(letras_descobertas)
        acertou = True
        nomeCom = "Competidor ", nomeC
        nomeDes = "Desafiante ", nomeD
        vencedor = nomeCom
        perdedor = nomeDes

        for x in range(0, len(letras_descobertas)):
            if letras_descobertas[x] == "*":
                acertou = False

        if errou == True:
            vida = vida -1
            print("Você errou! Você possui ", vida, "vidas.")

            if vida <= 0:
                print("Suas vidas acabaram!")
                acertou = True
                vencedor = nomeDes
                perdedor = nomeCom