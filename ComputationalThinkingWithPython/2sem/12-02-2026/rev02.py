fila = []

while True:
    print(f"\nFila: {fila}")
    opcao = input("1-Adicionar, 2-Executar, 3-Sair: ")

    if opcao == '1':
        demanda = input("Demanda: ")
        fila.append(demanda)
        print(f"Posição: {len(fila)}")
    
    elif opcao == '2':
        if fila:
            print(f"Executando: {fila.pop(0)}")
        else:
            print("Fila vazia.")
            
    elif opcao == '3':
        break