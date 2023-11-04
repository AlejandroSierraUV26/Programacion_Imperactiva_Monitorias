# #Preventiva
# while(True):
#     try:
#         numero = int(input("Ingrese un numero : "))
#         print(numero)
#         break
#     except ValueError: 
#         print("No se permite una letra")
#     except ZeroDivisionError:
#         print("No se permite dividir por 0")


def calcularSalario(numero):
    return numero * - 1

if __name__ == "__main__":
    while(True):
        try: 
            salario = int(input("Ingrese su salario : "))
            salario_nuevo = calcularSalario(salario)
            if salario_nuevo < 0:
                raise Exception
            else:
                print("Salario nuevo : ", salario_nuevo)
                break
        except ValueError:
            print("Solo puede ingresar un numero.")
        except: 
            print("El salario no puede ser negativo :", salario_nuevo)





