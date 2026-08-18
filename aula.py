print("Bem-vindo à sua pockédex de bolso")
nome = input("Digite o nome do seu pockemon: ")

quantidade_letras = len(nome)

print(f"O nome do seu pockemon tem {quantidade_letras} letras")

tipo = input("Digite o tipo do seu pockemon: ")

hp_pockemon = int(input("Digite o hp (vida) do seu pockemon: "))

peso_pockemon = float(input("Digite o peso do seu pockemon: "))

print("RELATÓRIO FINAL")
print("Nome: ", nome)
print("Tipo: ", tipo)
print("HP: ", hp_pockemon)
print("Peso: ", peso_pockemon)