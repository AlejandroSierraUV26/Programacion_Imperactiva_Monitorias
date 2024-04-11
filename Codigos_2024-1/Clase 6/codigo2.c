#include <stdio.h>
#include <stdlib.h>

int function(int num){
    if (num<=1) return 1;
    for (int i = 2; i * i <=num; i++)
        if (num % i == 0) return 1;
    return 0;
}
int main (){
    int arreglo[]={2,5,6,8,9,11,12,15};
    int tamano = 8;
    printf("Secuencia A: ");
    for (int i=0; i < tamano; i++)
    if (!function(arreglo[i])){
        printf (" %d ", arreglo[i]);
        arreglo[i]=-1;
    }
    printf("\nsecuencia B: ");
    for(int i=0;i<tamano;i++){
        if(arreglo[i]!=-1 && arreglo[i]%2!=0){
            printf(" %d ",arreglo[i]);
            arreglo[i] = -1;
        }
    }
    printf("\nArreglo final:");
    for(int i = 0; i<tamano;i++)
        printf(" %d ",arreglo[i]);
return 0;
}