print ("Olá")

nome = input("Digite seu nome: ")
ano = int(input("Digite o ano do seu nascimento: "))
ende = input("Digite seu endereço: ")
idade = 2025 - ano
frete = 20
vin1 = 25.00
vin2 = 40.00
vin3 = 60.00
vin4 = 100.00
vin5 = 150.00

if idade < 18:
    print("É PROIBIDO A VENDA DE BEBIDAS ALCOOLICAS PARA MENORES DE IDADE")

print("Esses são os vinhos que temos disponiveis:")
print("[1] Vinho nº 1 = R$ 25,00")
print("[2] Vinho nº 2 = R$ 40,00")
print("[3] Vinho nº 3 = R$ 60,00")
print("[4] Vinho nº 4 = R$ 100,00")
print("[5] Vinho nº 5 = R$ 150,00")
escolha = int(input("Digite o numero referente ao vinho que deseja: "))
quant = int(input("Digite a quantidade de garrafas que deseja: "))

if escolha == 1:
    vf = vin1 * quant
if escolha == 2:
    vf = vin2 * quant
if escolha == 3:
    vf = vin3 * quant
if escolha == 4:
    vf = vin4 * quant
if escolha == 5:
    vf = vin5 * quant

#Frete
if vf < 150.00:
    vf = vf + frete

#Desconto para clientes 60 anos ou mais
if idade >= 60:
    print("Cliente com 60 anos ou mais ganham um desconto de 5%")    
    desc = vf * 5 / 100
    vf = vf - desc

print("Agradeçemos pela sua compra, ", nome)
print("Será entregue no endereço: ", ende)
print("O valor final é de: ", vf)