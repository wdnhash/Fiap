consumo = int(input("Digite quantos kWh foram consumidos: "))
tipo = input("Digite o tipo de instalação: ")

if tipo == "R":
    if consumo > 500:
        vf = consumo * 0.65
    elif consumo <= 500:
        vf = consumo * 0.40

if tipo == "C":
    if consumo > 1000:
        vf = consumo * 0.55
    elif consumo <= 1000:
        vf = consumo * 0.60

if tipo == "I":
    if consumo > 5000:
        vf = consumo * 0.55
    elif consumo <= 5000:
        vf = consumo * 0.60
        
print(vf)