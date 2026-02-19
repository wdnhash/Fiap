n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
ope = input("Digite o simbolo da operação que deseja realizar: ")

if ope == "+":
    vf = n1 + n2
elif ope == "-":
    vf = n1 - n2
elif ope == "*":
    vf = n1 * n2
elif ope == "/":
    vf = n1 / n2
else:
    print("Tente novamente")

print("Valor final: ", vf)