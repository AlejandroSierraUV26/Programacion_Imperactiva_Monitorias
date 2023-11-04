
def puntaje_mayor(nombre_equipo):
    cantidad_participante = 2
    puntos_totales = 0
    puntaje_mas_alto = 0
    persona_mas_alto = ""
    i = 0
    while(i<cantidad_participante):
        personaje = input("Ingrese el nombre del participante : ")
        puntos = int(input("Ingrese los puntos: "))
        puntos_totales += puntos
        if puntos > puntaje_mas_alto : 
            puntaje_mas_alto = puntos
            persona_mas_alto = personaje
        i+=1
    return puntos_totales,(f"La persona con más puntos fue {persona_mas_alto} del equipo {nombre_equipo} con {puntaje_mas_alto} puntos")

def puntos_equipo_mayor(eq1,nomb1,eq2,nomb2,eq3,nomb3):
    if eq1 > eq2 and eq1 > eq3:
        return f"El equipo {nomb1} obtuvo más puntos: {eq1}"
    elif eq2 > eq1 and eq2 > eq3:
        return f"El equipo {nomb2} obtuvo más puntos: {eq2}"
    elif eq3 > eq2 and eq3 > eq1:
        return f"El equipo {nomb3} obtuvo más puntos: {eq3}"
    else:
        return f"Dos o todos los equipos obtuvieron los mismos puntos"
    
    
if __name__ == "__main__":   
    equipo1 = input("Ingrese el nombre del equipo 1 :")
    puntaje1,personaje1 = puntaje_mayor(equipo1)
    equipo2 = input("Ingrese el nombre del equipo 2 :")
    puntaje2,personaje2 = puntaje_mayor(equipo2)
    equipo3 = input("Ingrese el nombre del equipo 3 :")
    puntaje3,personaje3 = puntaje_mayor(equipo3)



    print(f"""
        {personaje1}
        
        {personaje2}
        
        {personaje3}

        Equipo {equipo1} / Puntos : {puntaje1}

        Equipo {equipo2} / Puntos : {puntaje2}
        
        Equipo {equipo3} / Puntos : {puntaje3}
        
        {puntos_equipo_mayor(puntaje1,equipo1,puntaje2,equipo2,puntaje3,equipo3)}
        """)        