"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. """


preco_morango = int(input('Digite o preço do morango: '))
preco_maca = int(input('Digite o preço da maçã: '))

quantidade_morango = float(input('Quantidade de morangos (Kg): '))
quantidade_maca = float(input('Quantidade de maças (Kg): '))

valor_total = (quantidade_morango * preco_morango) + (quantidade_maca * preco_maca)
valor_original = valor_total

if valor_total > 25 or quantidade_morango + quantidade_maca > 8:
  valor_total = valor_total - (valor_total * 10 / 100)
  print(f'Você tem direito a um desconto de 10%!')
  print(f'Valor original da compra: R$ {valor_original}')
  print(f'Valor final com desconto: R$ {valor_total}')
else:
  print(f'Valor a ser pago: R$ {valor_total}')
