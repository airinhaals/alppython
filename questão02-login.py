while True:
    print("####################")
    print("===== LOGIN =====")
    print("####################")

    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin" and senha == "123":

        print("\nLogin realizado! Bem-vindo, admin!")

        while True:

            print("\n===== MENU =====")
            print("1 - Cadastrar usuário")
            print("2 - Listar usuários")
            print("3 - Alterar usuário")
            print("4 - Excluir usuário")
            print("5 - Logout")
            print("6 - Encerrar")

            opcao = input("Escolha uma opção: ")

            if opcao == "5":
                print("Logout realizado!")
                break

            elif opcao == "6":
                print("Programa encerrado!")
                break

            else:
                print("Opção ainda não disponível.")

        if opcao == "6":
            break

    else:
        print("Usuário ou senha incorretos!")
