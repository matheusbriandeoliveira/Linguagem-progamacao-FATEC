"""Escreva um algoritmo para ler 10 números.
Todos os números lidos com valor inferior a 40 devem ser somados.
Escreva o valor final da soma efetuada. """

soma = 0
# Loop para ler os 10 números
for i in range(10):
    num = int(input(f"Insira um valor para o {i+1} número de (10) : "))
    if num < 40:
        soma = soma + num

# Exibindo a soma
print("A soma dos números inferiores a 40 é:", soma)