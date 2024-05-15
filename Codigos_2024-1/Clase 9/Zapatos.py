
zapatos = {"Adidas" : 
        [38,39,40,41,42]
 ,"Nike":
        [38,39,40,41,42]}

marca = "Adidas"
calzado = 42
valores = zapatos.get(marca)
print(zapatos)
for i in range(0,len(valores)):
    if valores[i] == calzado:
        valores.remove(calzado)

print(zapatos)
print(valores)    

            