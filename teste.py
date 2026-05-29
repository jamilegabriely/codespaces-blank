#Formula para calcular a força
def calcular_forca (peso, altura):
    forca = peso / (altura * altura) 
    return forca 
    
#Calculando o nível de força 
def verificar_nivel(forca): 
    if forca >= 20: 
        return "Nível 10"
    elif forca >= 10: 
        return "Nível 5" 
    else: 
        return "Nível 1" 

#Função principal
def main (): 
    print ("\n--- Sistema de calculo de força ---") 
    continuar = "sim" 
    while continuar == "sim": 

        #Cadastro personagens
        nome = input("\nDigite o nome do personagem: ") 
        gênero = input("Digite o gênero do personagem: ") 
        idade = input("Digite a idade do personagem: ")


        peso= float(input("Digite o peso do personagem (em kg): ")) 
        altura= float(input("Digite a altura (em metros): ")) 
        
        forca_calculada = calcular_forca(peso, altura) 
        nivel_final = verificar_nivel(forca_calculada) 
        
        print("\n----- RESULTADO -----") 
        print(f"Personagem: {nome}") 
        print(f"Gênero: {gênero}") 
        print(f"Idade: {idade}") 
        print(f"Força calculada: {forca_calculada:.2f}") 
        print(f"Classificação: {nivel_final}") 
        print("---------------------") 
  
        continuar = input("\nDeseja calcular novamente? (sim/nao): ").lower()
main()  