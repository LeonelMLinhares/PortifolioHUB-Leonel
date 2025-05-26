import random

print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente adivinhar o número entre 1 e 100!")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        print("Tente um número MAIOR!")
    else:
        print("Tente um número MENOR!")