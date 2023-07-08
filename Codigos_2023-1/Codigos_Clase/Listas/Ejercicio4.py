letras = ["A", "B", "C", "D", "E", "F", "G", 
          "H", "I", "J", "K", "L", "M", "N", 
          "Ñ", "O", "P", "Q", "R", "S", "T", 
          "U", "V", "W", "X", "Y", "Z"]
letras2 = []
for i in range(0,len(letras)):
    if i%3 != 0 or i == 0:
        letras2.append(letras[i])
print(letras2)

for i in (letras):
    if letras.index(i)%3 ==0:
        letras.remove(i)
letras.insert(0,"A")
print(letras)
        