# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

# variaveis 

soma = contador = 0

# agora o bixo pega

while True:
    numero = float(input("Digite um número (ou -1 para encerrar): "))
    
    if numero == -1:
        break
    
    soma += numero
    contador += 1

# exibir

print(f"A média dos números inseridos é: {soma / contador}" if contador > 0 else "Nenhum número foi inserido.")

# cabo