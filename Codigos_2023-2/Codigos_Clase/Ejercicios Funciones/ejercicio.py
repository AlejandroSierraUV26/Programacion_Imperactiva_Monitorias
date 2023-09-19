
"""

git status

git add .
git commit -m "Comentario"
git push

"""


"""
Diseñar una funcion que haga lo siguiente.
Calcular el area de un triangulo.

"""

def AreaTriangulo(v1,v2):
    return v1 * v2 / 2
area1 = AreaTriangulo(10,5)
area2 = AreaTriangulo(20,2)

print("AreaTriangulo1: ", area1)
print("AreaTriangulo2: ", area2)
     
     
"""
Diseñar una funcion que realice el calculo de un tanque 
de agua.

Tener en cuenta que el base y la altura es de 5 metros respectivos.

Determinar la cantidad maxima del tanque.

Para los valores de la profundidad siendo

pf = 5
?>125 m^3

pf2 = 10 
?>250 m^3

pf3 = 100
?>2500 m^3

"""
    
def VolumenTanque(profundidad):
    base = 5
    altura = 5
    return base * altura * profundidad

print(VolumenTanque(5))
print(VolumenTanque(10))
print(VolumenTanque(100))


