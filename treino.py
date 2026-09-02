# lava - jato

nome = input("Digite o nome do cliente: ")

print("\nTipos de lavagens disponíveis:")
print("1 - Simples     (R$ 30,00)")
print("2 - Completa    (R$ 50,00)")
print("3 - Especial    (R$ 80,00)")

tipo = input("Escolha o tipo de lavagem: ")
quantidade = int(input("Digite quantos carros serão lavados: "))

match tipo:
    case "1" | "Simples":
        custo = 30.0
        tipo_nome = "Simples"

    case "2" | "Completa":
        custo = 50.0
        tipo_nome = "Completa"

    case "3" | "Especial":
        custo = 80.0
        tipo_nome = "Especial"

    case _:
        print("\nOpção inválida, definindo taxa como R$ 0.00 por padrão.")
        custo = 0.0
        tipo_nome = "Inválido"

subtotal = custo * quantidade

if quantidade >= 3:
    desconto = subtotal * 0.15
else:
    desconto = 0.0

valor_final = subtotal - desconto

if valor_final <= 50:
    lavagem = "Básica"
elif valor_final <= 120:
    lavagem = "Intermediária"
else:
    lavagem = "Premium"


print("Conferindo os dados")
print(f"Nome do cliente: {nome}")
print(f"Tipo de lavagem: {tipo_nome}")
print(f"Quantidade de carros: {quantidade}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Valor final: {valor_final:.2f}")
print(f"Classificação: {lavagem}")