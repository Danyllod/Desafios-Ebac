
#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
#O usuário deverá informar a quantidade de CDs e o valor para cada um.

#Lembre-se de que você já tem a habilidade de desenvolver variáveis, estruturar dados, criar condições, repetições e funções. 

def calcular_investimento_cd():
    # Solicita a quantidade de CDs
    quantidade_cds = int(input("Informe a quantidade de CDs na coleção: "))
    
    # Inicializa o valor total investido
    valor_total = 0.0
    
    # Loop para solicitar o valor de cada CD
    for i in range(quantidade_cds):
        valor_cd = float(input(f"Informe o valor do CD {i + 1}: "))
        valor_total += valor_cd
    
    # Calcula o valor médio gasto por CD
    if quantidade_cds > 0:
        valor_medio = valor_total / quantidade_cds
    else:
        valor_medio = 0.0
    
    # Exibe os resultados
    print(f"Valor total investido na coleção: R${valor_total:.2f}")
    print(f"Valor médio gasto por CD: R${valor_medio:.2f}")

# Chama a função para executar o programa
calcular_investimento_cd()
