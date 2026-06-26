altura1 = float(input("Digite a primeira estatura: "))
altura2 = float(input("Digite a segunda estatura: "))
altura3 = float(input("Digite a terceira estatura: "))
                
if altura1 == altura2 or altura1 == altura3 or altura2 == altura3:
    print("Há, pelo menos, duas pessoas com a mesma altura")

elif altura1 > altura2 and altura1 > altura3:
    print(f"A maior estatura é {altura1:.2f}")

elif altura2 > altura1 and altura2 > altura3:
    print(f"A maior estatura é {altura2:.2f}")

else:
    print(f"A maior estatura é {altura3:.2f}")
