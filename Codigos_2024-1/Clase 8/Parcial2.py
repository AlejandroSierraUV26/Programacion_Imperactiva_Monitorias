
def construir_piramide(bloques):        
    altura = 0
    bloques_restantes = bloques 
    while bloques_restantes >= 0:
        altura += 1
        bloques_restantes -= altura
    return altura -1


for i in range(11):
    print(i,construir_piramide(i))
    

    



