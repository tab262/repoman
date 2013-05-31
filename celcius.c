#include <stdio.h>

int main()
{
    float celcius;
    printf("Please enter the celcius value: ");
    scanf("%f",&celcius);
    
    float fahrenheit = (9.0/5)*celcius + 32;
    printf("The temp %.3f Celcius is %.3f in fahrenheit\n", celcius, fahrenheit);
    
    return 0;
}
