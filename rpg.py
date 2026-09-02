#Apresentação inicial

print(" --- Bem Vindos ao RPG Jornada do Herói --- ")

print("\nSeu herói iniciou o jogo com uma poção vida!")
bonus = "Poção de vida extra"

#Coletando os dados do jogador
print("\nAdicione as informações do seu guerreiro: ")
nome = input("Digite o nome do herói: ")

print("O Jogo tem as seguintes classes disponiveis:")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")
print("4 - Ladino")
  
classe = input("Qual classe você deseja: ")

#Identificando pelo nome ou número da classe escolhida
if classe == "Guerreiro" or classe == "1":
    vida = 120
    ataque = 18
    defesa = 12
    mana = 0
elif classe == "Mago" or classe == "2":
    vida = 80
    ataque = 22
    defesa = 4
    mana = 50
elif classe == "Arqueiro" or classe == "3":
    vida = 100
    ataque = 20
    defesa = 8
    mana = 10
elif classe == "Ladino" or classe == "4":
    vida = 90
    ataque = 16
    defesa = 6
    mana = 20
else:
    print("\nOpção Inválida")
    print("O Jogo tem as seguintes classes disponiveis:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")
    print("4 - Ladino")

    classe = input("Digite uma dessas classes: ")


print("\nMenu principal do jogo")
print("1- Ver ficha do personagem")
print("2- Ir para uma batalha")
print("3- Ir à loja")
print("4- Salvar e sair do jogo")

menu = input("\nEscolha uma etapa do menu: ")

#Match case
match menu:
    case "1" | "Ver ficha do personagem":
        nome_tipo = "Ver ficha do personagem"

    case "2" | "Ir para uma batalha":
        nome_tipo = "Ir para uma batalha"

    case "3" | "Ir à loja":
        nome_tipo = "Ir à loja"

    case "4" | "Salvar e sair do jogo":
        nome_tipo = "Salvar e sair do jogo"

    case _: 
        print("\nTipo inválido!")
        tipo_nome = "Inválido"
    
print("\n--- Conferindo dados do guerreiro--- ")
print(f"Nome do héroi: {nome}")
print(f"Bônus recebido: {bonus}")
print(f"Classe escolhida: {classe}")
print(f"Vida do personagem: {vida}")
print(f"Ataque do personagem: {ataque}")
print(f"Defesa do personagem: {defesa}")
print(f"Mana do personagem: {mana}")