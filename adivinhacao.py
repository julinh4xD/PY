print ("*********************************")
print ("Bem vindo no jogo de adivinhação!")
print ("*********************************")

numero_secreto = 21
chute = input("Digite o seu número: ")

print ("Você digitou", chute)

if(numero_secreto == int(chute)):
    print("Você acertou!")
else:
    print("Você errou :(")

print("Fim do jogo")