n1 = int(input('Digite o inicio da sequencia: '))
n2 = int(input('Digite o fim da sequencia: '))
soma = 0
i = n1

while n1 <= n2:
    print(i)
    i += 1

for i in range(n2):
    print(i)

for s in range(n2):
    soma = soma + s

print(soma, soma/len(range(n1,n2+1)))