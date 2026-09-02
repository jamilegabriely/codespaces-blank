#sistema de loja

nome = input("Digite o nome do produto: ")

print("\nTipos de categorias disponíveis:")
print("1 - Eletrônicos")
print("2 - Roupas")
print("3 - Livros")

categoria = input("Digite qual categoria você deseja ir: ")
preco = float(input("Digite qual o preço do seu produto: "))
quantidade = int(input("Quantos você quer: "))

match categoria:
    case "1" | "Eletrônicos":
        tipo_nome = "Eletrônicos"

    case "2" | "Roupas":
        tipo_nome = "Roupas"

    case "3" | "Livros":
        tipo_nome = "Livros"

    case _:
        tipo_nome = "Formato inválido"

subtotal = preco * quantidade   

if tipo_nome == "Eletrônicos" and quantidade >= 3:
    desconto = subtotal * 0.15
elif tipo_nome == "Roupas" and subtotal > 100.0:
    desconto = subtotal * 0.10
elif tipo_nome == "Livros" and quantidade >= 5:
    desconto = subtotal * 0.05
else:
    desconto = 0.0

valor_final = subtotal - desconto

print("Conferindo dados do guerreiro")
print(f"Nome do héroi: {nome}")
print(f"Classe escolhida: {tipo_nome}")
print(f"Quantidade: {quantidade}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Valor final: {valor_final:.2f}")