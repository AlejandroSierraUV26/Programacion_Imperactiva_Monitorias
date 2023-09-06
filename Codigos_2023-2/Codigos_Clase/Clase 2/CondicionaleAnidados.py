"""
Comision por venta
Venta: Entero
    1. 10%
    2. 20%
    3. 35%
    4. 45%
    5. 50%
    6. 60%
    


"""

ventas = float(input("Ingrese las ventas realizadas : "))

categoria = int(input("Categoria : "))

if categoria == 1: 
    comision = ventas * 0.10
elif categoria == 2:
    comision = ventas * 0.20
elif categoria == 3:
    comision = ventas * 0.35
elif categoria == 4:
    comision = ventas * 0.45
elif categoria == 5:
    comision = ventas * 0.50
elif categoria == 6:
    comision = ventas * 0.60
else:
    comision = 0
    
print("La comision es : ", comision)