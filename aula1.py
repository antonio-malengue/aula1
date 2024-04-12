print("Digita seu nome: ")
nome = input()

print("Digita seu salário: ")
salario = float(input())

print("Digita seu bônus: ")
bonus = float(input())

resultado = round(1000 + (salario*bonus), 2)

print(f"Saudações {nome}!!! O seu salário com Bônus é {resultado} Kz")