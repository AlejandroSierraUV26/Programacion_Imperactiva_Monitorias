def forma_expandida(num):
    num_str = str(num)
    partes_expandidas = []
    
    for i, digito in enumerate(num_str):
        if digito != '0':
            ceros = len(num_str) - i - 1
            valor_posicion = digito + '0' * (ceros)
            partes_expandidas.append(valor_posicion)
    
    forma_expandida_str = ' + '.join(partes_expandidas)
    
    return forma_expandida_str

print(forma_expandida(12))      # Debería devolver '10 + 2'
print(forma_expandida(42))      # Debería devolver '40 + 2'
print(forma_expandida(70304))   # Debería devolver '70000 + 300 + 4'
