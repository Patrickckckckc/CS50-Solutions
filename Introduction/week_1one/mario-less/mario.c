#include <cs50.h>
#include <stdio.h>

int height;
int input_height(void);
void pyramids_hash_dot(int number);
int main(void)
{
    // Prompt for input for the height (1-8)
    height = input_height();
    // Print the height of the pyramids
    for (int row = 1; row <= height; row++)
    {
        pyramids_hash_dot(row);
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
void pyramids_hash_dot(int number)
{
    for (int dot = height; dot > number; dot--)
    {
        printf(" ");
    }
    for (int hash = 0; hash < number; hash++)
    {
        printf("#");
    }
    printf("\n");
}
