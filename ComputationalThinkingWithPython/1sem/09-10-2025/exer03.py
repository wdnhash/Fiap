soma = 0

while True:
    n1 = int(input('Digite um numero: '))
    if n1 == 0:
        break
    soma = soma + n1
print(f'Soma total dos valores digitados {soma}')