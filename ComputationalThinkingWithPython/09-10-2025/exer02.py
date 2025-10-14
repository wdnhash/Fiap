a = int(input('Digite um numero: '))
b = 1

while b < a:
    b = b + 1
    c = b % 2
    if c == 0:
        print(b)
