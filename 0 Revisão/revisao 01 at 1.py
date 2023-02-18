def verificar(a,b,c):
    if a == b == c:
        return ('Triângulo Equilátero')
    elif a == b or b == c or a == c:
        return('Triângulo Isósceles')
    else:
        return ('Triângulo Escaleno')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

print("Tipo de triângulo:", verificar(a, b, c))
