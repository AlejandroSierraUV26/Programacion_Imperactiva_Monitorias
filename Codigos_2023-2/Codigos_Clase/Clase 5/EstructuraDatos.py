"""
Se le presenta la siguiente situacion:

    Debe almacenar todos las edades de los estudiantes de un curso de programacion
    
Si esta pensando hacer cada edad en una variable, dejeme decirle que no es del todo
eficiente. 
Porque imaginese que en un salon esten matriculados más de 150 personas.
¿Cree que es eficiente hacer 150 variables para almacenar las edades de cada uno?

La respuesta es no. Por eso existen las estructuras de datos, que son un conjunto,
una lista, un diccionario, tublas, etc.

Y en python como en muchos lenguajes de programación nos permiten almacenar n numeros
en una sola variable interable.

En este caso veremos las listas y los diccionarios.

Una lista puede almacenar numeros, strings, booleanos, etc.

Ejemplo: 

edad = [1, 2, 3, 4, 5,20,21,29]

Para nosotros definir desde un principio que queremos una lista debemos usar las llaves
¨[ ]", esto nos permitira acceder a la informacion que necesitemos

Si quisiera acceder al primer elemento de la lista edad.
Seria algo asi:

edad[0] # Esto me retornaria 1

Siempre inicia desde 0 hasta n-1, refiendose al ultimo elemento de la lista.

"""

"""
Ejemplo 1:

Almacenar al menos 5 nombres dentro de una lista y mostrarlos por pantalla.
    
"""

# nombres = ["Alejandro", "Maria", "Carlos" , "Juan" , "Pablo "]

# # Para mostrar todos los elementos en Python es muy sencillo.

# print(nombres)



"""
Conjuntos 

Los conjuntos en la programacion tienen un gran peso en el mismo.

La teoria de conjuntos nos indica que deben ser elementos contables.

Si un elemento se repite se toma solo uno, cosa que no pasa en las listas.

Ejemplo 2: 

    Numeros mayores de 10 y menores que 20
    10<=numero<=20
    
    numeros = {11,12,13,14,15,16,17,18,19,20}
    
Tambien esta la opcion de referirnos a un rango de numeros.

La palabra reservada range() nos permite definir un conjunto de numeros.

Sus argumentos son: 
    Primero: El numero inicial del conjunto
    Segundo: El numero final del conjunto -1
    range(10,20)
Y si probamos verificar si hay un numero dentro de ese rango con la palabra reservada "in"

Que nos permite verificar si hay un numero en un conjunto, retornando un valor booleano.


> 15 in range(10,20) --> True

> 10 in range(10,20) --> True

> 20 in range(10,20) --> False

> 8 in range(10,20) --> False

"""

"""
Tuplas

Las tuplas son los elementos de estructuras de control inmutables, quiere decir que sus elementos no
pueden ser afectados de ninguna manera, mientras que en las listas por ser mutables, puede agregar, eliminar
y demas.

Las tuplas se definen con parentesis "()" y sus elementos se separan por comas ","

Para acceder a los elementos de una tupla se hace de la misma manera que en las listas, con la diferencia
que no se puede modificar.



Ejemplo 3 :

    tupla = (1,2)
    
    ?numero1 = tupla[0]
    
    ó 
    
    ?numero1, numero2 = tupla
    ?numero1, numero2 = (1,2)
    




"""