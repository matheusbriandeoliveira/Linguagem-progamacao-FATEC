"""#Instruções
A escola “APRENDER” faz o pagamento de seus professores por hora/aula.
Faça um algoritmo que calcule e exiba o salário de um professor.

Sabe-se que o valor da hora/aula segue a tabela abaixo:

Professor Nível 1 R$12,00 por hora/aula
Professor Nível 2 R$17,00 por hora/aula
Professor Nível 3 R$25,00 por hora/aula """



print('Digite o nível do professor [01] [02] [03]:')
nivel = int(input())

hr_trab = int(input('Informe as horas trabalhadas: '))

if nivel == 1:
    valor_hr = 12
elif nivel == 2:
    valor_hr = 17
else:
    valor_hr = 25

salario = valor_hr * hr_trab
print("O salário é de R$", salario)