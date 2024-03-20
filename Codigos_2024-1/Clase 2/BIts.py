def suma_binaria(num1, num2):
    resultado = bin(int(num1, 2) + int(num2, 2))[2:]
    return resultado

def resta_binaria(num1, num2):
    resultado = bin(int(num1, 2) - int(num2, 2))[2:]
    return resultado

def multiplicacion_binaria(num1, num2):
    resultado = bin(int(num1, 2) * int(num2, 2))[2:]
    return resultado

def division_binaria(num1, num2):
    if num2 == '0':
        return "Error: División por cero"
    resultado = bin(int(num1, 2) // int(num2, 2))[2:]
    return resultado

def main():
    num1 = int(input("Ingrese el primer número binario: "))
    num2 = int(input("Ingrese el segundo número binario: "))
    operacion = input("Ingrese la operación a realizar (+, -, *, /): ")

    if len(num1) != len(num2):
        print("Error: Los números binarios deben tener la misma longitud.")
        return

    if operacion == '+':
        print("Resultado:", suma_binaria(num1, num2))
    elif operacion == '-':
        print("Resultado:", resta_binaria(num1, num2))
    elif operacion == '*':
        print("Resultado:", multiplicacion_binaria(num1, num2))
    elif operacion == '/':
        print("Resultado:", division_binaria(num1, num2))
    else:
        print("Operación no válida")

if __name__ == "__main__":
    main()
