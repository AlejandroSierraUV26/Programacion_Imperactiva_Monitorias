import random
import time

def funcion():
    lista = []
    i = 0

    while i<8: 
        numero_aleatorio = random.randint(16,20)
        if numero_aleatorio == 20: #1
            if 20 in lista:  
                continue
            else:
                lista.append(numero_aleatorio)
        elif numero_aleatorio == 19: # 2
            if 19 in lista:
                if lista.count(19) == 2:
                    continue
                else:
                    lista.append(numero_aleatorio)
            else:
                lista.append(numero_aleatorio)
        elif numero_aleatorio == 18: #1
            if 18 in lista:
                continue
            else:
                lista.append(numero_aleatorio)
        elif numero_aleatorio == 17: #3
            if 17 in lista:
                if lista.count(17) == 3:   
                    continue
                else:
                    lista.append(numero_aleatorio)
            else:
                lista.append(numero_aleatorio)
        elif numero_aleatorio == 16: # 1
            if 16 in lista:
                continue
            else:
                lista.append(numero_aleatorio)
                
        i+=1
            
    print(lista)


# Medir el tiempo de la funcion


start_time = time.time()


funcion()


print("--- %s seconds ---" % (time.time() - start_time))


