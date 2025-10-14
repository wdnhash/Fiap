veloc = int(input("Qual a velocidade do carro: "))
limite = 80
valorMulta = 5
valorPagar = 0

if veloc > limite:
    valorPagar = (veloc - 80) * 5
    print("A valor total da Multa é de R$ ", valorPagar)
else:
    print("Parabens, você é uma lesma kkk")