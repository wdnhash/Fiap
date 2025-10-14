segt = 100000

segf = segt % 60
minu = segt // 60
minf = minu % 60
hora = minu // 60
horaf = hora % 24
dia = hora // 24

print("Dias:", dia)
print("Horas:", horaf)
print("Minutos:", minf)
print("Segundos:", segf)