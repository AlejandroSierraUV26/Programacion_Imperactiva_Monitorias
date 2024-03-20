"""
Se tienen 6000 dias y 1230 meses

año = 365 dias
meses = 30 dias

Representrarlo de una manera mas legible

"""

dias = 6000
meses =1230

meses = meses + dias // 30
dias = dias % 30

años = meses // 12
meses = meses % 12





print(f"Años :{años}")
print(f"Meses :{meses}")
print(f"Dias :{dias}")


# segundos = 120
# minutos = 120
# horas= 0

# minutos = minutos + segundos // 60
# segundos = segundos % 60
# horas = horas + minutos // 60

# minutos = minutos % 60

# print(f"Horas :{horas}")
# print(f"Minutos :{minutos}")
# print(f"Segundos :{segundos}")

