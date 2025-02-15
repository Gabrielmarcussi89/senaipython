senha = "abcd1234"

senhadigitada = ""

while senhadigitada != senha:
    senhadigitada = input("Digite a senha : ")
    if senhadigitada != senha:
        print("Senha inválida")

print("Senha correta")

