#Calcular gastos de viagem

#Formula para calcular custos
def calcular_gastos (hospedagem, alimentacao, lazer):

    gastos = hospedagem + alimentacao + lazer

    return gastos

#Função para ver quanto sobra ou falta no orçamento
def calcular_orcamento (total, gastos):

    orcamento = total - gastos

    return orcamento

#Avaliar viagem
def avaliar_viagem(orcamento):

    if orcamento >= 0:

       return "Orçamento suficiente!"

    else:

        return "Orçamento inuficiente."



def main ():

    print ("\n-------Calcular Gastos de Viagem-------")

    continuar = "sim"

    while continuar == "sim":

       

        valor_total = float(input("\nDigite o valor total que você possui: "))

        valor_hospedagem = float(input("Digite o preço da hospedagem: "))

        valor_alimentacao = float(input("Digite o valor destinado à alimentação: "))

        valor_lazer = float(input("Digite o valor destinado ao lazer: "))



        total_gastos = calcular_gastos(valor_hospedagem, valor_alimentacao, valor_lazer)

        orcamento_calculado = calcular_orcamento(valor_total, total_gastos)

        resultado_avaliacao = avaliar_viagem(orcamento_calculado)



        print("\n------- RESULTADO -------")

        print(f"Dinheiro Disponível: R$ {valor_total:.2f}")

        print(f"Total de Gastos: R$ {total_gastos:.2f}")

        print(f"Saldo Restante: R$ {orcamento_calculado:.2f}")

        print(f"Avaliação da Viagem: {resultado_avaliacao}")  

        print("---------------------")

 

        continuar = input("\nDeseja calcular novamente? (sim/nao): ").lower()

main()  
