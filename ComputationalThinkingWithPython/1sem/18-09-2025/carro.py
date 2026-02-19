kmPerco = int(input("Digite quantos kilometros foram percorrridos: "))
dias = int(input("Digite quantos dias você ficou com o carro: "))

diasPass = 60
kmRoda = 0.15

valorTotal = kmPerco * kmRoda + dias * diasPass

print("Valor total a pagar: R$ ", valorTotal)
