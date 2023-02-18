'''Faça um programa em Python que leia uma String e dois caracteres.
Troque todas as ocorrências do primeiro caractere (podendo ser maiúsculo ou minúsculo)
pelo segundo e imprima a quantidade de vezes que o caractere foi substituído.  '''

contador = 0
string = input("Digite uma string: ")

caractere1 = input("Digite o caractere a ser substituído: ")
caractere2 = input("Digite o caractere de substituição: ")

caractere1 = caractere1.lower()
caractere2 = caractere2.lower()


nova_string = ""
for letra in string:
    if letra.lower() == caractere1:
        nova_string += caractere2
        contador += 1
    else:
        nova_string += letra

# imprime a nova string com as substituições
print("Nova string:", nova_string)

# imprime a quantidade de substituições
print("Quantidade de substituições:", contador)

