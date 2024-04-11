#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a;
    printf("Ingrese valor: ");
    scanf("%d", &a);
    for (int i=1; i<=a; i++){
        for (int j=1; j<=a-i; j++)printf(" ");
            for (int k=1; k<=2*i-1; k++)printf("*");
            printf("\n");
    }

    return 0;
}