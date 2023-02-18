'''1 - Faça um programa em Python que leia um nome e o escreva tantas vezes quantos forem seus caracteres. Um nome por linha. '''

nome = input("Digite um nome: ")

linha = "".join(nome)

for letra in nome:
    print(linha)