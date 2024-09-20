#include <stdio.h> // Incluimos la librería estándar de entrada y salida de datos
/*

    Numeros : 
    Int -> 4 bytes -> -2,147,483,648 to 2,147,483,647 
    Double -> 8 bytes -> 1.7
    Float -> 4 bytes -> 1.7
    Char -> 1 byte -> 'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z' 'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J' 'K' 'L' 'M' 'N' 'O' 'P' 'Q' 'R' 'S' 'T' 'U' 'V' 'W' 'X' 'Y' 'Z' '0' '1' '2' '3' '4' '5' '6' '7' '8' '9' ' ' '!' '"' '#' '$' '%' '&' '(' ')' '*' '+' ',' '-' '.' '/' ':' ';' '<' '=' '>' '?' '@' '[' '\' ']' '^' '_' '`' '{' '|' '}' '~'

    String -> 1 byte * n -> "Hola mundo"

    Operadores :
        + Suma
        - Resta
        * Mult
        / Division 
        % Modulo 
        ++ Incremento
        -- Decremento
        += Asignacion con suma
        -= 
        *= 
        /= 
        %= 
        == igual a 
        != diferente de
        > 
        < 
        >= 
        <= 
        && And
        || Or
        ! Negacion
        & And binario -> 1 & 1 = 1, 
                        1 & 0 = 0, 
                        0 & 1 = 0, 
                        0 & 0 = 0
        | Or binario -> 1 | 1 = 1, 
                        1 | 0 = 1, 
                        0 | 1 = 1, 
                        0 | 0 = 0
        ^ Xor binario -> 1 ^ 1 = 0, 
                        1 ^ 0 ^ 1 ^ 1 ^ 1 ^ 1 ^ 0 = 1,
                        0 ^ 1 = 1, 
                        0 ^ 0 = 0
        ~ Not binario -> ~1 = 0, 
                        ~0 = 1
    Funciones: 

    void -> No retorna nada
    int -> Retorna un entero
    float -> Retorna un flotante
    double -> Retorna un double
    char -> Retorna un char
    string -> Retorna un string
    
    void nombreFuncion(){
        Codigo
    }
    
    int nombreFuncion(){
        Codigo
        return 0;
    }

    int nombreFuncion(int a, int b, float c, double d, char e){
        Codigo
        return 0;
    }
    int main(){
        Codigo
        return 0;
    }

    if (condicion){
        Codigo

    }
    else if (condicion){
        Codigo
    }
    else{
        Codigo
    }

    switch (variable){
        case 1:
            Codigo
            break;
        case 2:
            Codigo
            break;
        case 3:
            Codigo
            break;
        case 4:
            Codigo
            break;
        default:
            Codigo
            break;
    }

    for (int i = 0; i < 10; i++){
        Codigo
    }
    
    while (condicion){ # 0 o mas veces
        Codigo
    }

    do{ # 1 o mas veces
        Codigo
    }while(condicion);

    i = 0;
    while (i < 10){
        printf("%d",i);
        i++;
    }
*/


#include <stdio.h>
#include <stdlib.h>
int funcion(int numA){
  if(numA<=1){ 
    return 1; // verdadero
  }
  else{
    for(int i=2;i<=numA/2;i++){
        if(numA%i==0){
            return 1;  // verdadero
        } 
    }
    return 0; // falso
  }
   
}

int main(){
    int A,B;
    A = 1;
    B = 20;
    printf("Resultado: \n");
    for(int i = A; i <=B;i++){
        if (!funcion(i)){
            printf("%d",i);
            printf("\n");
        }            
    }
        
    return 0;
}

