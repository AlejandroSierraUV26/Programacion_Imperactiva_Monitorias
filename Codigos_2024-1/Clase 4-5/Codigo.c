#include <stdio.h>
#include <stdlib.h>

int funcion(int numA){
if(numA<=1) return 1;
for(int i=2;i<=numA/2;i++)
    if(numA%i==0)
    return 1;
return 0;
}
int main()
{
    int A,B;
      printf("Resultado: \n");
      for(int i = A; i <=B;i++)
      if (funcion(i))
        printf("%d",i);
    return 0;
}