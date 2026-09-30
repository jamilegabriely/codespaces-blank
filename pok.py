import random
import time

def fase1_treino():
    print("\nFASE 1: TREINO")
    pontos_experiencia = 0

    for sessao in range(1,6):
        pontos_obtidos = random.randint(5,20)
        pontos_experiencia += pontos_obtidos
        print(f"Sessão {sessao}: Seu pokemon ganhou {pontos_obtidos} pontos")
        time.sleep(0.3)

    print(f"\nTotal de treino: {pontos_experiencia} pontos.")
    return pontos_experiencia

def fase2_lider_ginasio(pontos_experiencia):
    print("\nFASE 2: LÍDER DE GINÁSIO")

    lider_hp = 100
    pokemon_hp = 70
    turno = 1

    bonus_ataque = pontos_experiencia/20

    print(f"O Pókemon do líder do ginásio aparece com {lider_hp} pontos de vida!")
    print(f"Seu bonus de ataque é: {bonus_ataque}\n")

    while lider_hp > 0 and pokemon_hp > 0:
        print(f"Turno: {turno}")

        dano_jogador = random.randint(8,15) + bonus_ataque
        lider_hp -= dano_jogador
        lider_hp =  max(lider_hp, 0)
        print(f"Seu pókemon atacou, causando {dano_jogador} de dano!")
        print(f"HP atual do líder: {lider_hp}")

        if lider_hp <= 0:
            print("\nO pokemon do lider foi derrotado! Você venceu o desafio")
            break
            
        dano_lider = random.randint(8,12)
        pokemon_hp -= dano_lider
        pokemon_hp =  max(pokemon_hp, 0)
        print(f"O líder atacou, causando {dano_lider} de dano!")
        print(f"HP atual do pokemon: {pokemon_hp}")

        if pokemon_hp <= 0:
            print("\nO seu pokemon foi derrotado! Você perdeu o desafio")
            break

        turno += 1
        time.sleep(0.3)

    return pokemon_hp > 0


def fase3_reiniciar_desafio():
    while True:
        print("INÍCIO DO DESAFIO: GINÁSIO POKÉMON")

        pontos_experiencia = fase1_treino()
        venceu = fase2_lider_ginasio(pontos_experiencia) 

        print("\nFIM DO DESAFIO")
        if venceu:
            print("Parábens, você conquistou a insígnia do ginásio!")
        else:
            print("Seu pokémon foi derrotado. Tente novamente!")

        resposta = input("Deseja reiniciar o desafio? (s/n): ").strip().lower()
        if resposta != "s":
            print("Obrigada por jogar!")
            break

if __name__ == "__main__":
    fase3_reiniciar_desafio()