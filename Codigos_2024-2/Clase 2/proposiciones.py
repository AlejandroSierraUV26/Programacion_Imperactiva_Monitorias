def letras_binarias():
    letras = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    binarios = [bin(i - ord('A') + 1)[2:] for i in range(ord('A'), ord('Z')+1)]
    return dict(zip(letras, binarios))

letras_en_binario = letras_binarias()
for letra, binario in letras_en_binario.items():
    print(f"{letra}: {binario}")
    
    
def frase_a_binario(frase):
    letras_en_binario = letras_binarias()
    frase_binaria = ""
    for letra in frase:
        if letra.upper() in letras_en_binario:
            frase_binaria += letras_en_binario[letra.upper()] + " "
        else:
            frase_binaria += " "
    return frase_binaria.strip()

frase = "PASAME LA TAREA NECESITO PASAR PROGRAMACION"
frase_binaria = frase_a_binario(frase)
print(frase_binaria)