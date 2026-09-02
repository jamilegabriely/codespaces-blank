print("--- Bem vindo ao Sistema de Lanchonete --- ")

#cadastrando cliente 
nome = input("Digite o nome do cliente: ")
valor = float(input("Digite o valor do pedido: "))
entrega = input("Digite qual tipo de entrega você escolheu: ")

#identificando os tipos de entrega
match entrega:
    case "Padrão":
        custo = 5

    case "Expressa":
        custo = 10

    case "Agendada":
        custo = 7

    case "Retirada":
        custo = 0

    case _:
        print("Tipo inválido")

#calculando o valor final
valor_final = valor + custo

#classificando o pedido
if valor_final < 30:
    categoria = "Pedido pequeno"
elif valor_final <= 60:
    categoria = "Pedido médio"
else:
    categoria = "Pedido grande"

#confirmando os dados
print("--- Conferindo os dados --- ")
print(f"Nome do cliente: {nome}")
print(f"Valor dos produtos: R$ {valor:.2f}")
print(f"Taxa de entrega: R$ {custo:.2f}")
print(f"Valor Final: R$ {valor_final:.2f}")
print(f"Classificação do cliente: {categoria}")