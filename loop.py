limite = 101
contador = 0

sair = False

while sair == False:
    print('contando.: ', contador)
    contador += 1 

    resposta = input('Deseja parar o contador? S/N: ')

    if resposta == "N":
       sair = False
    else: 
       sair = True


print('Final da contagem')
