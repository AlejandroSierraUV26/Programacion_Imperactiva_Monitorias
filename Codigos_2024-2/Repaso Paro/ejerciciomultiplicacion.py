import random


contador = 0
for i in range(10):
    while True:            
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        if num1 == 3 or num2 == 3 or num1 == 5 or num2 == 5:
            continue
        else:
            break
        
    print(f"Cuanto es : {num1} x {num2} =" )
    respuesta = int(input("Ingrese la respuesta : "))
    
    if respuesta == (num1* num2):
        contador +=1
        print("Correcto esa es la respuesta")
        
    else:
        print(f"Incorrecto, era : {num1*num2}")
    
    


print(f"Su puntaje es :{contador}")
    