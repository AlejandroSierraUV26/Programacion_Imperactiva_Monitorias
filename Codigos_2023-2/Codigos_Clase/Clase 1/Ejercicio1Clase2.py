cedula = str(input("Ingrese su cedula: "))
año = int(input("Ingrese el año de vinculacion : "))
descuento = 0
salario = float(input("Ingrese su salario: "))

if ((salario>1_200_000) and (año>1990)):
    descuento = 8/100
if ((salario<550_000) or (año==1990)):
    descuento = 2/100
    
salario_nuevo = salario-(salario*descuento)

print(salario_nuevo)