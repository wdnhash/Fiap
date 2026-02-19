idade = 19
salario = 1500
amigoDoDono = True

idamin = 18
salmin = 3000

idaempres = idade >= idamin
salempre = salario >= salmin

empres = (idaempres and salempre) or amigoDoDono

print("O cliente pode contratar o emprestimo: ", empres)