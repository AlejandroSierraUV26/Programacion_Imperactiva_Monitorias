"""
    Encuentra todas las palabras en una lista que comienzan con una letra específica.

    Args:
    - lista_palabras (list): Lista de palabras a ser analizadas.
    - letra (str): Letra con la que deben comenzar las palabras.

    Returns:
    - palabras_encontradas (list): Lista de palabras que cumplen con el criterio.
"""


def buscar_ocurrencias(cadena, palabra):
    ocurrencias = []
    indice = -1

    cadena = cadena.lower()
    palabra = palabra.lower()

    while True:
        indice = cadena.find(palabra, indice + 1)

        if indice == -1:
            break

        ocurrencias.append(indice)

    return ocurrencias


cadena_texto = "Python es un lenguaje de programación muy poderoso. Es también fácil de aprender."

palabra_buscada = "python"

posiciones_ocurrencias = buscar_ocurrencias(cadena_texto, palabra_buscada)

print(f"Cadena de texto: {cadena_texto}")
print(f"Palabra buscada: {palabra_buscada}")
print(f"Posiciones de ocurrencias: {posiciones_ocurrencias}")
