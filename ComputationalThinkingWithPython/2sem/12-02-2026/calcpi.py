def calcular_pi(termos):
    pi = 0
    denominador = 1
    operacao = 1

    for _ in range(termos):
        pi += operacao * (4 / denominador)
        denominador += 2
        operacao *= -1
        
    return pi

resultado = calcular_pi()
print(f"Valor aproximado de Pi: {resultado}")