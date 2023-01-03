
#include <stdio.h>

void discount(float price, int percentage);

int main(void)
{
    float regular = get_float("Regular price: \n")
    int percent_off =  get_int("Percent off: \n")
    int sale = discount(regular, percent_off)
    printf("Sale price: %.2f\n" sale)
  
}

void discount(folt price, int percentage)
{
    return price * (100 - percentage) / 100
}
