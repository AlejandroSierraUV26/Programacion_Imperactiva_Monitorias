Funcion factoriao(numero)
    acc <- 1
    Para i <- 1 Hasta numero Con Paso 1 Hacer
        acc <- acc * i
    FinPara
    Retornar acc
FinFuncion
SubProceso tabla_multiplicar(numero)
    Escribir "Tabla de multiplicar del ", numero
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir numero, " x ", i, " = ", numero * i
    FinPara
FinSubProceso
SubProceso par_impar(numero)
    Si numero % 2 = 0 Entonces
        Escribir "El numero: ", numero, " es par"
    Sino
        Escribir "El numero: ", numero, " no es par"
    FinSi
FinSubProceso
Funcion Es_primo(numero) Como Logico
    acc <- 0
    Para i <- 2 Hasta numero-1 Con Paso 1 Hacer
        Si numero % i = 0 Entonces
            acc <- acc + 1
        FinSi
    FinPara
    
    Si acc = 0 Entonces
        Retornar Verdadero
    Sino
        Retornar Falso
    FinSi
FinFuncion
Funcion siguiente_primo(numero)
    num <- numero
    acc <- 1
    Mientras No Es_primo(numero+acc) Hacer
        num <- num + 1
        acc <- acc + 1
    FinMientras
    Retornar num + 1
FinFuncion
