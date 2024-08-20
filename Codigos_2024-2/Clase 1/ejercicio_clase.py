"""

Realizar un ejercicio donde se le pregunte a una persona
sobre su informacion personal y que dependiento de sus respuestas
pregunte mas o pregunte menos


Ejemplo:

Nombre : Juan
Edad : 20
Peso : 70
Altura : 1.70
Casado : False

1. Si la persona es mayor de 18 años, preguntar si tiene hijos
2. Si la persona tiene hijos, preguntar cuantos hijos tiene
4. Si la persona esta casada, preguntar hace cuanto tiempo esta casado
5. Si la persona no esta casada, preguntar si tiene pareja
6. Si la persona tiene pareja, preguntar hace cuanto tiempo esta con su pareja
7. Si la persona no tiene pareja, preguntar si tiene mascotas
8. Si la persona tiene mascotas, preguntar cuantas mascotas tiene
9. Si la persona no tiene mascotas, preguntar si vive solo
10. Si la persona vive solo, preguntar hace cuanto tiempo vive solo
11. Si la persona no vive solo, preguntar con cuantas personas vive
12. Si la persona vive con mas de 3 personas, preguntar si le gusta vivir con tanta gente
13. Si la persona vive con menos de 3 personas, preguntar si le gusta vivir con tanta gente

14. Si la persona es menor de 18 años, preguntar si esta estudiando
15. Si la persona esta estudiando, preguntar que carrera esta estudiando
16. Si la persona no esta estudiando, preguntar si trabaja
17. Si la persona trabaja, preguntar en que trabaja
18. Si la persona no trabaja, preguntar si esta buscando trabajo
19. Si la persona esta buscando trabajo, preguntar hace cuanto tiempo esta buscando trabajo
20. Si la persona no esta buscando trabajo, preguntar si le gustaria trabajar
21. Si la persona le gustaria trabajar, preguntar en que le gustaria trabajar


"""


nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
casado = bool(input("Ingrese si esta casado: "))
texto_final = ""


if edad>=18:
    hijos = str(input("Tiene hijos ? : "))
    if hijos == "si":
        cantidad_hijos = int(input("Cuantos hijos tiene ? : "))
        texto_final = f"Usted tiene {cantidad_hijos} hijos"
    else:
        casado = str(input("Esta casado ? : "))
        if casado == "si":
            tiempo_casado = int(input("Hace cuanto tiempo esta casado ? : "))
            texto_final = f"Usted esta casado hace {tiempo_casado} años"
        else:
            pareja = str(input("Tiene pareja ? : "))
            if pareja == "si":
                tiempo_pareja = int(input("Hace cuanto tiempo esta con su pareja ? : "))
                texto_final = f"Usted esta con su pareja hace {tiempo_pareja} años"
            else:
                mascotas = str(input("Tiene mascotas ? : "))
                if mascotas == "si":
                    cantidad_mascotas = int(input("Cuantas mascotas tiene ? : "))
                    texto_final = f"Usted tiene {cantidad_mascotas} mascotas"
                else:
                    vive_solo = str(input("Vive solo ? : "))
                    if vive_solo == "si":
                        tiempo_vive_solo = int(input("Hace cuanto tiempo vive solo ? : "))
                        texto_final = f"Usted vive solo hace {tiempo_vive_solo} años"
                    else:
                        cantidad_personas = int(input("Con cuantas personas vive ? : "))
                        if cantidad_personas > 3:
                            gusta_vivir = str(input("Le gusta vivir con tanta gente ? : "))
                            texto_final = f"Usted vive con {cantidad_personas} personas y le gusta vivir con tanta gente"
                        else:
                            gusta_vivir = str(input("Le gusta vivir con tanta gente ? : "))
                            texto_final = f"Usted vive con {cantidad_personas} personas y le gusta vivir con tanta gente"
else:
    estudia = str(input("Esta estudiando ? : "))
    if estudia == "si":
        carrera = str(input("Que carrera esta estudiando ? : "))
        texto_final = f"Usted esta estudiando {carrera}"
    else:
        trabaja = str(input("Trabaja ? : "))
        if trabaja == "si":
            trabajo = str(input("En que trabaja ? : "))
            texto_final = f"Usted trabaja en {trabajo}"
        else:
            busca_trabajo = str(input("Esta buscando trabajo ? : "))
            if busca_trabajo == "si":
                tiempo_busqueda = int(input("Hace cuanto tiempo esta buscando trabajo ? : "))
                texto_final = f"Usted esta buscando trabajo hace {tiempo_busqueda} años"
            else:
                gusta_trabajar = str(input("Le gustaria trabajar ? : "))
                if gusta_trabajar == "si":
                    trabajo = str(input("En que le gustaria trabajar ? : "))
                    texto_final = f"Usted le gustaria trabajar en {trabajo}"
                else:
                    texto_final = "Usted no quiere trabajar"
print(texto_final)
