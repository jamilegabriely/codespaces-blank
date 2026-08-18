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
ano_destino = int(input("Para qual ano você deseja viajar?"))
print(f"Bem-vindo(a), {nome}! Seu identificador tem {len(nome)} letras.")
print(f"Ano atual do sistema: {ano_atual} | Bateria: {bateria}%")

#CÁLCULO DA VIAGEM
distancia_anos = abs(ano_destino - ano_atual)
bateria_necessaria = distancia_anos * CONSUMO_POR_ANO

print(f"Distância calculada: {distancia_anos} anos.")
print(f"Bateria necessária para o salto: {bateria_necessaria}%")

#DESAFIO
if bateria >= bateria_necessaria:
    print("Bateria suficiente! Viajando no tempo...")
    
    # Atualiza as variáveis do jogo
    bateria -= bateria_necessaria  
    ano_atual = ano_destino
    
    print(f"Sucesso! Você chegou ao ano {ano_atual}.")
    print(f"Bateria restante: {bateria}%")

else:
    print("Bateria insuficiente para completar o salto!")
    print("A nave desligou no meio do caminho e você ficou preso na fenda temporal!")
    print("Para gerar energia de emergência, você precisa resolver um desafio do sistema.")
    
    # DESAFIO DE EMERGÊNCIA
    print("--- DESAFIO: Estabilização de Frequência ---")
    codigo = int(input("Digite um número PAR qualquer para recalibrar os painéis solares: "))
    
    if codigo % 2 == 0:
        print("CÓDIGO CORRETO! Painéis solares ativados!")
        bateria += 30.0
        ano_atual = ano_destino
        print(f"Você conseguiu pousar no ano {ano_atual} com {bateria}% de bateria de emergência!")
    else:
        print("CÓDIGO INCORRETO! O sistema travou completamente.")
        ficou_preso = True

# 6. RELATÓRIO FINAL DO SISTEMA
print("       --- RELATÓRIO DA MISSÃO ---           ")


# Operador lógico NOT
if not ficou_preso:
    print(f"Status: MISSÃO BEM SUCEDIDA! {nome} está seguro(a) no ano {ano_atual}.")
else:
    print(f"Status: PERDIDO NO TEMPO! {nome} não conseguiu reativar a nave.")

print("nome:", (nome))
print("ano_atual:", (ano_atual))
print("bateria:", (bateria))
print("ficou_preso:", (ficou_preso))