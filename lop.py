import random
import time

def fase1_caca_tesouro(): 
    print("\nFASE 1: CAÇA AO TESOURO")
    moedas = 0

    for escavar in range(1,6):
        moedas_encontradas = random.randint(5,20)
        moedas += moedas_encontradas
        print(f"Escavação {escavar}: você encontrou {moedas_encontradas} moedas de ouro") 
        time.sleep(0.3)

    print(f"\nTotal encontrado: {moedas} moedas de ouro.")
    return moedas

def fase2_kraken(moedas):
    print("\nFASE 2: KRAKEN")
    kraken_hp = 100
    navio_hp = 60
    turno = 1
    
    bonus_canhao = moedas/2

    print(f"o Kraken emergiu das profundezas com {kraken_hp} pontos de vida!")
    print(f"Seu bônus de canhão é {bonus_canhao}\n")

    while kraken_hp > 0 and navio_hp > 0:
        print(f"Turno {turno}")

        #Ataque do navio
        dano_navio = random.randonit(8,15) + bonus_canhao
        kraken_hp -= dano_navio
        kraken_hp = max(kraken_hp, 0)
        print(f"Seus canhões dispararam causando {dano_navio} de dano!") 
        print(f"Hp atual do kraken: {kraken_hp}")

        if kraken_hp <= 0:
            print("\nO kraken foi derrotado!")
            break

        #Ataque do kraken
        dano_kraken = random.randint(5,12)
        navio_hp -= dano_kraken
        navio_hp = max(navio_hp, 0)
        print(f"O kraken golpeia o navio causando {dano_kraken} de dano")
        print(f"HP atual do navio: {navio_hp}")

        if navio_hp <= 0:
            print("\nSeu navio afundou. O kraken venceu...")

            turno += 1
            time.sleep(0.3)

        return navio_hp > 0

def fase3_reiniciar_viagem():
    while True:
        print("\nINICIO DA VIAGEM")

        moedas = fase1_caca_tesouro()
        venceu = fase2_kraken(moedas)

        print("\nFIM DA VIAGEM")
        if venceu:
            print("Parábens, você derrotou o kraken e garantiu seu tesouro!")
        else:
            print("Seu navio afundou. Tente novamente!")

        resposta = input("\nDeseja reinciar a viagem? (s/n)").strip().lower()
        if resposta != "s":
            print("\nObrigada por jogar! Até a próxima!")
            break

if __name__== "__main__":
    fase3_reiniciar_viagem