#Apresentação inicial
print("--- Bem-vindo ao sistema de classificação de jogadores ---")

print("\nAdicione as informações do seu jogador: ")

nome = input("Digite o nome do seu jogador: ")
pontuacao = int(input("Digite a pontuação do seu jogador: "))
atributo = input("Digite o atributo do seu jogador:\n1. Força\n2. Agilidade\n3. Inteligência\nOutro: ")
nivel = float(input("Digite em qual nível seu jogador está: "))

#Definindo um bônus pelo nível
if nivel <= 30:
    print("Bônus: Você não tem acesso ao bônus de vida!")
elif nivel <= 70:
    print("Bônus: Você tem acesso a +20% de vida!")
else:
    print("Bônus: Você tem acesso a +50% de vida!")

# Estrutura do match-case correta
match atributo:
    case "Força":
        print("Efeito: Você recebeu Força Bruta (+10 de Dano).")
    case "Agilidade":
        print("Efeito: Você recebeu Esquiva (+15% Velocidade).")
    case "Inteligência":
        print("Efeito: Você recebeu Mente Aberta (+20% Mana).")
    case "Outro":
        extra = input("Digite o nome do seu atributo personalizado: ")
        print(f"Efeito: Atributo extra '{extra}' registrado com sucesso!")
    case _:
        print("Opção inválida!")

#Verificando dados
print("\n--- Conferindo os dados ---")
print("nome:", (nome))
print("pontuaca:", (pontuacao))
print("atributo:", (atributo))
print("nivel:", (nivel))
