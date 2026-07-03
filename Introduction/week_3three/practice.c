#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int array[3][3];
    for (int i = 0; i < 3; i++)
    {
        for(int a = 0; a < 3; a++)
        {
             int value = get_int("Number: ");
             array[i][a] = value;
        }
    }
}
