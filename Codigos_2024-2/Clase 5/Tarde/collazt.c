#include <stdio.h>
#include <stdlib.h>

// Prototipos de funciones
void collatz(int n); // Inicializacion 

int main() {
    int numero;

    printf("Ingrese un número entero positivo: ");
    if (scanf("%d", &numero) != 1 || numero <= 0) {
        printf("Entrada no válida. Por favor ingrese un número entero positivo.\n");
        return 1;
    }

    printf("Secuencia de Collatz para %d:\n", numero);
    collatz(numero);

    return 0;
}

void collatz(int n) {
    while (n != 1) {
        printf("%d ", n);
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    printf("1\n");
}