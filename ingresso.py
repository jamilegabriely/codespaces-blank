print ("\n--- Cadastro de igressos online ---")

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
estudante = input("Você é estudante? (sim/não): ").lower()
responsavel = input("Está acompanhado de um responsável? (sim/não): ").lower()
aceitou_termos = input("Você aceita os termos do site? (sim/não): ").lower()
valor_ingresso = float(input("Digite o valor do ingresso:"))

#BOOLEANO
if responsavel == "sim":
    tem_reponsavel = True
else:  
    tem_reponsavel = False


if estudante == "sim":
    cliente_premium = True
else:  
    cliente_premium = False


if aceitou_termos == "sim":
    aceitou = True
else:
    aceitou = False


#VERIFICANDO
if idade < 16 and not tem_reponsavel:
    print ("Ingresso cancelado!")
    print ("Motivo: menores de 16 anos precisam de um responsável")
else:
    print ("Liberado!")

if idade <= 18 or cliente_premium:
    print ("Você tem acesso a área premium!")
else:
    print ("Você não tem acesso a área premium!")

if not aceitou:
    print ("Ingresso negado")
    print ("Motivo: não aceitou os termos do site")
else:
    print ("Ingresso confirmado!")

if estudante and <= 17:
    desconto = valor_ingresso * 0.2
    valor_final = valor_ingresso - desconto

    print ("\n--- Desconto de 20 por cento aceito ---")
    