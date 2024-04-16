

# Loop infinito para validar o nome do utilizador
while True:
    # Solicita ao utilizador para digitar seu nome
    print("Digite seu nome: ")
    nome = input()
    # Verifica se o nome contém apenas letras
    if nome.replace(" ", "").isalpha():
        break
    else:
        print("Erro: O nome deve conter apenas letras.")

# Loop infinito para solicitar ao utilizador que digite seu salário até que um valor válido seja fornecido
while True:
    try:
        # Solicita ao utilizador para digitar seu salário e converte para float
        print("Digite seu salário: ")
        salario = float(input())
        # Verifica se o salário é negativo e lança uma exceção se for
        if salario < 0:
            raise ValueError("Salário inválido. Digite um valor positivo.")
        # Sai do loop se um valor válido for fornecido
        break
    except ValueError as e:
        # Captura e exibe a mensagem de erro se um valor inválido for fornecido
        print(f"Erro: {e}")

# Loop infinito para solicitar ao utilizador que digite seu bônus até que um valor válido seja fornecido
while True:
    try:
        # Solicita ao utilizador para digitar seu bônus e converte para float
        print("Digite seu bônus: ")
        bonus = float(input())
        # Verifica se o bônus está fora do intervalo [0, 1] e lança uma exceção se estiver
        if bonus < 0 or bonus > 1:
            raise ValueError("Bônus inválido. Digite um valor entre 0 e 1.")
        # Sai do loop se um valor válido for fornecido
        break
    except ValueError as e:
        # Captura e exibe a mensagem de erro se um valor inválido for fornecido
        print(f"Erro: {e}")

# Calcula o salário com bônus
resultado = round(1000 + (salario * bonus), 2)

# Exibe uma mensagem de saudação com o nome do utilizador e seu salário com bônus
print(f"Saudações, {nome}!!! Seu salário com bônus é de {resultado} Kz")