salario = float(input("Digite o salário: R$"))
cargo = input("Digite o cargo: ")

if cargo == "Programador de Sistemas":
    novo_salario = salario * 1.30
    print(f"Novo salário: R${novo_salario:.2f}")

elif cargo == "Analista de Sistemas":
    novo_salario = salario * 1.20
    print(f"Novo salário: R${novo_salario:.2f}")

elif cargo == "Analista de Banco de Dados":
    novo_salario = salario * 1.15
    print(f"Novo salário: R${novo_salario:.2f}")
    
else:
    print("Cargo inválido")
