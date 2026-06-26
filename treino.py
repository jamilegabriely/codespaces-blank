print ("\n--- Bem vindo ao hotel Costa Branca ---")

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
dias = int(input("Quantos dias você vai ficar no hotel? "))
responsavel = input("Está acompanhado de um responsável? (sim/não): ").lower()
vip = input("Você é cliente VIP? (sim/não): ").lower()
aceitou_regras = input("Você aceita as regras do hotel? (sim/não): ").lower()

if responsavel == "sim":
    tem_reponsavel = True
else:  
    tem_reponsavel = False

if vip == "sim":
    cliente_vip = True
else:  
    cliente_vip = False

if aceitou_regras == "sim":
    aceitou = True
else:
    aceitou = False

#REGRA 1: Concordar com as regras do hotel
#NOT

if not aceitou:
    print ("Reserva cancelada!")
    print ("Motivo: não aceitou as regras do hotel")

#REGRA 2: menores de 18 precisam de um responsável
#AND = NOT
elif idade < 18 and not tem_reponsavel:
    print ("Reserva cancelada!")
    print ("Motivo: menores de 18 precisam de um responsável")

else:
    print ("Reserva aceita!")

#REGRA 3: três ou mais diárias OU vip = café da manhã
#OR

if dias >= 3 or cliente_vip:
    print ("Café da manhã incluso!")
else:
    print ("Reserva aceita sem café da manhã incluso")

#REGRA 4: sete ou mais dias E ser vip = quarto melhor
#AND

if dias >= 7 and cliente_vip:
    print ("Parabéns! Upgrade de quarto liberado")
else:
    print ("Quarto padão reservado!")
