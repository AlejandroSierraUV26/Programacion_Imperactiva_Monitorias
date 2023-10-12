

numero_productos = int(input("Ingrese la cantidad de productos : "))

acomulador1 = 0
acomulador2 = 0
acomulador3 = 0

for i in range(0,numero_productos):
    producto = int(input("Ingrese la categoria : \n 1. Postres \n 2. Panes \n 3. Bebidas \n :"))
    precio = float(input("Ingrese el precio : "))
    if producto == 1:
        acomulador1 += precio
    elif producto == 2: 
        acomulador2 += precio
    elif producto == 3: 
        acomulador3 += precio
    else: 
        print("Categoria no valida")
        
print("Total: ", acomulador1 + acomulador2 + acomulador3)