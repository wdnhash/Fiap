fila = ['joao', 'maria', 'carlos', 'euclides']

ar = input('Digite 1 para adiconar a fila ou 0 para remover: ')

if ar == '0':
    fila.pop(0)
    print(fila)
elif ar == '1':
    fila.append(input('Digite o nome do cliente que vai entrar na fila: '))
    print(fila)
else:
    print('Codigo invalido')