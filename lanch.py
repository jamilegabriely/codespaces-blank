#sistema de cinema

nome = input("Digite o nome do cliente: ")

print("\nTipos de ingresso disponíveis:")
print("1 - Inteira (R$ 20,00)")
print("2 - Meia    (R$ 10,00)")
print("3 - VIP     (R$ 35,00)")

tipo = input("Digite o tipo do ingresso: ")
quantidade = int(input("Digite quantos ingressos você deseja: "))

match tipo:
    case "1" | "Inteira":
        custo = 20.0
        tipo_nome = "Inteira"

    case "2" | "Meia":
        custo = 10.0
        tipo_nome = "Meia"

    case "3" | "VIP":
        custo = 35.0
        tipo_nome = "VIP"

    case _:
        print("\nTipo inválido! Definindo taxa como R$ 0.00 por padrão.")
        custo = 0.0
        tipo_nome = "Inválido"

subtotal = custo * quantidade

if quantidade >= 5:
    desconto = subtotal * 0.10
else:
    desconto = 0.0

valor_final = subtotal - desconto


if subtotal < 20:
    compra = "Compra pequena"
elif subtotal <= 60:
    compra = "Compra média"
else:
    compra =  "Compra grande"

print("Conferindo dados")
print(f"Nome do cliente: {nome}")
print(f"Tipo de ingresso: {tipo_nome}")
print(f"Quantidade de ingressos: {quantidade}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Valor final: {valor_final:.2f}")
print(f"Classificação: {compra}")