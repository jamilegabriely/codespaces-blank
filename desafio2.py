#Apresentação inicial
print("--- Bem-vindo ao sistema de classificação de delivery ---")

#Coletando os dados
nome = ("Digite o nome do cliente: ")
preco = float(("Digite quanto deu seu pedido (R$): "))
entrega = input("Digite o tipo de entrega que deseja:\n1. Retirada\n2. Padrão\n3. Expressa\n4. Agendada\nOpção: ")

# Definindo o custo de cada entrega
if entrega == "1" or entrega.lower() == "retirada":
    taxa_entrega = 0.0
    print("A entrega não custa nada.")
elif entrega == "2" or entrega.lower() == "padrão":
    taxa_entrega = 5.0
    print("A entrega padrão custa R$ 5,00.")
elif entrega == "3" or entrega.lower() == "expressa":
    taxa_entrega = 10.0
    print("A entrega expressa custa R$ 10,00.")
elif entrega == "4" or entrega.lower() == "agendada":
    taxa_entrega = 7.0
    print("A entrega agendada custa R$ 7,00.")
else:
    taxa_entrega = 5.0
    print("Opção inválida! Aplicando taxa padrão de R$ 5,00.")

#Calculo de quanto custou
preco_final: preco + entrega

#Classificando o cliente
if preco_final <= 20:
    bronze = True
elif preco_final <= 60:
    prata = True
else:
    ouro = True

#Usando o match case
match cliente:
    case "bronze"
    print(Você é nível bronze e nao possui beneficios extras no site)

    ...

#Verificando dados
print("\n--- Conferindo os dados ---")
print("nome:", (nome))
print("preco_final:", (preco_final))
print("entrega escolhida:", (entrega))



# Apresentação inicial
print("--- Bem-vindo ao sistema de classificação de delivery ---")

# Coletando os dados
nome = input("Digite o nome do cliente: ")
preco = float(input("Digite quanto deu seu pedido (R$): "))


# Cálculo do valor final
preco_final = preco + taxa_entrega

# Classificando o cliente de acordo com o valor final
if preco_final <= 20:
    categoria = "Bronze"
elif preco_final <= 60:
    categoria = "Prata"
else:
    categoria = "Ouro"

# Mensagem do benefício usando match-case
match categoria:
    case "Bronze":
        print("Você é nível Bronze e não possui benefícios extras no site.")
    case "Prata":
        print("Você é nível Prata e ganhou um cupom de 5% de desconto para o próximo pedido!")
    case "Ouro":
        print("Você é nível Ouro e ganhou frete grátis + 10% de desconto!")

# Imprimindo em tela todas as informações
print("\n--- RESUMO DO PEDIDO ---")
print(f"Nome do cliente: {nome}")
print(f"Valor dos produtos: R$ {preco:.2f}")
print(f"Taxa de entrega: R$ {taxa_entrega:.2f}")
print(f"Valor Final: R$ {preco_final:.2f}")
print(f"Classificação do cliente: {categoria}")