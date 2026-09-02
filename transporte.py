#Sistema de transporte de passageiros

nome = input("Digite o nome do passageiro: ")
idade = int(input("Digite a idade do passageiro: "))

print("\nA empresa oferece: ")
print("1 - ÔNIBUS (R$8,00 por km)")
print("2 - VAN (R$10,00 por km)")
print("3 - CARRO PARTICULAR (R$15,00 por km)")
print("4 - MOTO (R$5,00 por km)")

modalidade = input("Digite qual modalidade vc quer: ")
distancia = float(input("Digite a distância da viagem em km: "))

match modalidade:
    case "1" | "ÔNIBUS":
        custo = distancia * 8.0
        tipo_nome = "ÔNIBUS"
    
    case "2" | "VAN":
        custo = distancia * 10.0
        tipo_nome = "VAN"
    
    case "3" | "CARRO PARTICULAR":
        custo = distancia * 15.0
        tipo_nome = "CARRO PARTICULAR"

    case "4" | "MOTO":
        custo = distancia * 5.00
        tipo_nome = "MOTO"

    case _:
        custo = 0.0
        tipo_nome = "Opção inválida"

subtotal = custo

if idade < 12:
    desconto = custo * 0.50
elif idade <= 17:
    desconto = custo * 0.20
elif idade >= 60:
    if distancia > 50:
        desconto = custo * 0.40
    else:
        desconto = custo * 0.30
else:
    desconto = 0.0

valor_final = subtotal - desconto
    
print("Conferindo dados")
print(f"Nome do passageiro: {nome}")
print(f"Idade: {idade}")
print(f"Modalidade escolhida: {tipo_nome}")
print(f"Distância da viagem: {distancia:.2f} km")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Valor final: R${valor_final:.2f}")