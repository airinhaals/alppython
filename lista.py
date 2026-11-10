produtos = []

while True:
    produto = input("Digite o nome do produto eletrônico: ")
    produtos.append(produto)

    resposta = input("Deseja adicionar outro produto? (s/n): ").lower()

    if resposta == "n":
        break

print("\nLista de produtos eletrônicos:")

for produto in produtos:
    print(produto)
