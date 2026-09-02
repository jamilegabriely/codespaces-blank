#CONSTANTES
CAPACIDADE_MAX_BATERIA = 100.0  
CONSUMO_POR_ANO = 0.5           
ANO_INICIAL = 2026        

#VARIÁVEIS
ano_atual = 2026         
ano_destino = 0        
bateria = 100.0          
ficou_preso = False      

print("--- PAINEL DE CONTROLE - VIAGEM NO TEMPO ---")

#ENTRADA DE DADOS
nome = str(input("Digite o seu nome: "))
print(f"Bem-vindo(a), {nome}! Seu identificador tem {len(nome)} letras.")

while bateria > 0 and not ficou_preso:
    print(f"\nAno atual do sistema: {ano_atual} | Bateria: {bateria:,.1f}%")

    ano_destino = int(input("\nPara qual ano você deseja viajar?"))

    #CÁLCULO DA VIAGEM
    distancia_anos = abs(ano_destino - ano_atual)
    bateria_necessaria = distancia_anos * CONSUMO_POR_ANO

    print(f"\nDistância calculada: {distancia_anos} anos.")
    print(f"Bateria necessária para o salto: {bateria_necessaria:,.1f}%")

    #DESAFIO
    if bateria >= bateria_necessaria:
        print("\nBateria suficiente! Viajando no tempo...")
    
        # Atualiza as variáveis
        bateria -= bateria_necessaria  
        ano_atual = ano_destino
    
        print(f"Sucesso! Você chegou ao ano {ano_atual}.")
        print(f"Bateria restante: {bateria:,.1f}%")

    else:
        print("\nBateria insuficiente para completar o salto!")
        print("A nave desligou no meio do caminho e você ficou preso na fenda temporal!")
        print("Para gerar energia de emergência, você precisa resolver um desafio do sistema.\n")
    
        #DESAFIO DE EMERGÊNCIA
        print("--- DESAFIO: Recarregue a máquina ---")
        codigo = int(input("Digite um número PAR qualquer para recalibrar os painéis: "))
    
        if codigo % 2 == 0:
            print("\nCÓDIGO CORRETO! +30% de bateria!")
            bateria += 30.0
            ano_atual = ano_destino
            print(f"Você conseguiu pousar no ano {ano_atual} com {bateria:,.1f}% de bateria de emergência!")

        else:
            print("\nCÓDIGO INCORRETO! O sistema será encerrado.")
            ficou_preso = True

#RELATÓRIO FINAL DO SISTEMA
print("   --- RELATÓRIO DA MISSÃO ---   ")

if not ficou_preso and bateria > 0:
    print(f"Status: MISSÃO BEM SUCEDIDA! {nome} está seguro(a) no ano {ano_atual}.")
else:
    print(f"Status: PERDIDO NO TEMPO! {nome} não conseguiu reativar a nave.")

print("\n--- Conferindo os dados ---")
print("nome:", (nome))
print("ano_atual:", (ano_atual))
print("bateria:", (bateria))
print("ficou_preso:", (ficou_preso))