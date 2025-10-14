p1 = 0.50
p2 = 1.00
p3 = 4.00
p4 = 7.00
p5 = 8.00

vf = 0

while True:
    pro = input('Digite o produto que deseja: ')
    quant = input('Digite a quantidade de produtos: ')
    vf = vf + pro * quant
    if pro == 0:
        break
print(f'Valor a pagar: R${vf}')