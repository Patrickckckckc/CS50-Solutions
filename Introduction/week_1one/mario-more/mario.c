#include <cs50.h>
#include <stdio.h>

int input_height(void);
void pyramids_hash_dot(int number, int height);
int main(void)
{
    // Prompt for input for the height (1-8)
    int height = input_height();
    // Print the height of the pyramids
    for (int row = 1; row <= height; row++)
    {
        pyramids_hash_dot(row, height);
    }
}

// INPUT FUNCTION
int input_height(void)
{
    int num;
    do
    {
        num = get_int("Give me a number: (1-8)\n");
    }
    while (num < 1 || num > 8);
    return num;
}

// SPACE AND HASH FUNCTION
void pyramids_hash_dot(int number, int height)
{
    for (int dot = height; dot > number; dot--)
    {
        printf(" ");
    }
    for (int hash = 0; hash < number; hash++)
    {
        printf("#");
    }
    for (int value_0 = 0; value_0 < 2; value_0++)
    {
        printf(" ");
    }
    for (int hash = 0; hash < number; hash++)
    {
        printf("#");
    }
    printf("\n");
}
