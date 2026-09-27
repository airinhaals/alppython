import random

while True:
    print("JOGO DE ADIVINHAÇÃO")
    print("1 - Fácil (1 a 10)")
    print("2 - Médio (1 a 20)")
    print("3 - Difícil (1 a 30)")

    dificuldade = int(input("Escolha a dificuldade: "))

    if dificuldade == 1:
        limite = 10
    elif dificuldade == 2:
        limite = 20
    elif dificuldade == 3:
        limite = 30
    else:
        print("Opção inválida! Tente novamente.")

    sorteado = random.randint(1, limite)

    for tentativa in range(3):
        numero = int(input("Digite um número: "))

        if numero == sorteado:
            print("Parabéns, você acertou!")
            break

        elif numero < sorteado:
            print("Você errou!")
            print("Tente um número maior.")

        else:
            print("Você errou!")
            print("Tente um número menor.")

    else:
        print("Você perdeu! Fim de jogo.")
        print("O número sorteado era", sorteado)

    jogar = input("Quer jogar novamente? (s/n): ")

    if jogar != "s":
        break
