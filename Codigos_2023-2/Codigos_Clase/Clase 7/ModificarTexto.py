palabra = "Alejandro,Maria,Juan,Sebastian,Mario,Sara"

nombre = {"Alejandro": 19, "Maria": 20}

if "Alejandro" in palabra:
    print("Alejandro esta")
    palabra = palabra.replace("Alejandro,", "")
    
    print(palabra)

