import random

cantD_ = {
    20:2,
    19:9,
    18:4,
    17:5,
    16:20
}

lista = []

i = 0
while i<40:
    maquina = random.randint(16,20)
    if maquina == 20:
        if 20 in lista: # Asume que hay 1 o mas de 1 
            if lista.count(20) == cantD_[20]: # Asume 2 exactas
                continue
            else:
                lista.append(maquina) # Hay 1 
        else: # Asume que no hay ninguna
            lista.append(maquina)
    if maquina == 19:
        if 19 in lista: # Asume que hay 1 o mas de 1 
            if lista.count(19) == cantD_[19]: # Asume 2 exactas
                continue
            else:
                lista.append(maquina) # Hay 1 
        else: # Asume que no hay ninguna
            lista.append(maquina)
    if maquina == 18:
        if 18 in lista: # Asume que hay 1 o mas de 1 
            if lista.count(18) == cantD_[18]: # Asume 2 exactas
                continue
            else:
                lista.append(maquina) # Hay 1 
        else: # Asume que no hay ninguna
            lista.append(maquina)
    if maquina == 17:
        if 17 in lista: # Asume que hay 1 o mas de 1 
            if lista.count(17) == cantD_[17]: # Asume 2 exactas
                continue
            else:
                lista.append(maquina) # Hay 1 
        else: # Asume que no hay ninguna
            lista.append(maquina)
    if maquina == 16:
        if 16 in lista: # Asume que hay 1 o mas de 1 
            if lista.count(16) == cantD_[16]: # Asume 2 exactas
                continue
            else:
                lista.append(maquina) # Hay 1 
        else: # Asume que no hay ninguna
            lista.append(maquina)
            
    i+=1
    
    
for i in range(16,21):
    print(i, lista.count(i))
    