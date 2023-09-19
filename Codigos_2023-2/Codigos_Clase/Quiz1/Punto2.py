"""

La empresa de energía CELSIA que presta los servicios en la ciudad de Tuluá 
requiere recalcular la factura de energía de los consumidores. Para ello, se 
necesita de un programa que lea el estrato social y el valor de consumo del 
cliente, y determine el valor básico a adicionar para establecer el nuevo valor
de la factura.

	
El programa debe reportar el nuevo valor de la factura.  
Para saber los valores básicos que corresponde a cada categoría use la siguiente 
tabla:



"""


estracto = int(input("Ingrese su estracto : "))
valor_Consumo = float(input("Ingrese el valor de consumo : "))

valor_base = 0

if estracto == 1:
    valor_base = 500
elif estracto == 2:
    valor_base = 700
elif estracto == 3:
    valor_base = 4800
elif estracto == 4 :
    valor_base = 6700
else: 
    print("Categoria invalida")
    
if(estracto>=1 and estracto <=4):
    internet = (20/100) * valor_Consumo
    aseo = (12.20/100)* valor_Consumo

    valor_factura = valor_base + valor_Consumo + internet + aseo
    print("El valor de la factura es : ", valor_factura)

