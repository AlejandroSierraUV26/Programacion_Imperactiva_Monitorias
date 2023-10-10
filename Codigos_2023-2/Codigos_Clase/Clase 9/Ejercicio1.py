""""
La empresa El Barrigon S.A.S requiere un programa que permita calcular el sueldo
a pagar en un mes de trabajo, para este ejercicio vamos a suponer que un mes tiene 30 dias.

En la empresa tenemos tres tipos de trabajadores:
a) Ejecutivo: Tiene un salario base de $3.000.000
b) Administrativo: Tiene un salario base de $2.000.000
c) Auxiliar: Tiene un salario base de $1.500.000

El salario base considera las 192 horas que estan dentro de un tiempo completo de acuerdo a la
normativa laboral colombiana. Es de anotar que un trabajador no puede laboral menos de ese
tiempo, por lo que la funcion a diseñar debe emitir un mensaje cuando se ingrese un tiempo
menor.

Sin embargo, se pueden trabajar horas extras (es decir de la hora 193 en adelante) que se pagan
a un 20 % adicional del valor de la hora.

Ademas si el trabajador tiene mas de 5 años trabajando en la empresa recibe un bono adicional
correspondiente a un 20 % adicional su salario total (salario base + horas extras)

Ejemplo:

>>> A. Tipo trabajador: Administrativo
>>> B. Numero de horas trabajadas: 199
>>> C. Tiempo de trabajo: 8 años.

El salario seria

>>> Base mas horas extras(7 en total)
    2000000 + 1.2 * 7 * 10416.6666667 = 2087500
>>> Total con b o n i f i c a c i o n
    1.2 * (2087500)
>>> Salario total :
2505000

"""

def salario(cargo, horas_trabajadas,horas_extra,años_trabajador):
    if cargo == "Ejecutivo":
        salario_base = 3000000
    elif cargo == "Administrativo":
        salario_base = 2000000
    elif cargo == "Auxiliar":
        salario_base = 1500000
    else:
        print("Cargo no valido")
        return 0
    if horas_trabajadas >=192:
        salario_total = salario_base + (horas_extra*1.2) * (salario_base/192)
        if años_trabajador >= 5:
            salario_total = salario_total*1.2
        return salario_total
    else:
        print("Tiempo de trabajo no valido")
        return 0
    
nombre = "Alejandro"

cargo = "Administrativo"

horas = 192

horas_extra = 7

años_trabajados = 8


print(salario(cargo,horas,horas_extra,años_trabajados))


