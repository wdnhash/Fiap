#a = 'Eu tenho R$%10.2f reais' %x
#print(a)

x = 18.6984323456789
nome = 'Wenderson'
idade = 22
#a = 'Eu me chamo %s. Tenho %d anos. E tenho R$%.2f reais.'% (nome, idade, x)
a = 'Eu me chamo {}. Tenho {} anos. E tenho R${} reais.'.format(nome, idade, x)
b = 'Eu me chamo [{:-^11s}]'.format(nome)
c = f'Eu me chamo {nome:=^11s}. Tenho {idade} anos. E tenho R${x} reais.'
print(a)
print(b)
print(c)