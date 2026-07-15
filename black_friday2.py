while True:
    valor = float(input("\nDigite o valor da compra: "))
    print("-" * 50)

    opcao = int(input("""[1] À vista - 15% de desconto
[2] Cartão de débito - 10% de desconto
[3] Cartão de crédito - 5% de desconto
[0] Sair
Selecione a opção desejada: ""))

    print("-" * 50)

    if opcao == 0:
        print("Programa encerrado!")
        break

    elif opcao == 1:
        desconto = valor * 0.15
        total = valor - desconto
        print(f"O valor do desconto é de R${desconto:.2f} e o valor final a ser pago é de R${total:.2f}")

    elif opcao == 2:
        desconto = valor * 0.10
        total = valor - desconto
        print(f"O valor do desconto é de R${desconto:.2f} e o valor final a ser pago é de R${total:.2f}")

    elif opcao == 3:
        desconto = valor * 0.05
        total = valor - desconto
        print(f"O valor do desconto é de R${desconto:.2f} e o valor final a ser pago é de R${total:.2f}")

    else:
        print("Opção inválida!")
