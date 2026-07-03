#include <cs50.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>

const long ten_by13 = 1000000000000;
long input_creditcard(void);
int count_digit(long creditcard);
bool credit_algorytmus(long card_number, int cifra);
int main(void)
{
    // Prompt INPUT
    long creditcard = input_creditcard();

    // Function of Digits
    int cifra = count_digit(creditcard);

    // Calculate Checksum
    bool checksum = credit_algorytmus(creditcard, cifra);

    // Check for the card length and starting digits
    // Print AMEX, MASTERCARD, VISA
    if (checksum == true)
    {
        // AMEX
        if (cifra == 15)
        {
            long AMEX_start = creditcard / ten_by13 * 10;
            if (AMEX_start == 34 || AMEX_start == 37)
            {
                printf("AMEX\n");
            }
            else
            {
                printf("AMEX with different start\n");
            }
        }
        // MASTER CARD and VISA (16)
        else if (cifra == 16)
        {
            long MASTER_start = creditcard / ten_by13 * 100;
            long VISA_start = creditcard / ten_by13 * 1000;

            if (MASTER_start == 51 || MASTER_start == 52 || MASTER_start == 53 ||
                MASTER_start == 54 || MASTER_start == 55)
            {
                printf("MASTER CARD\n");
            }
            else if (VISA_start == 4)
            {
                printf("VISA CARD\n");
            }
        }
        // VISA (13)
        else if (cifra == 13)
        {
            long VISA_start = creditcard / ten_by13;
            if (VISA_start == 4)
            {
                printf("VISA CARD\n");
            }
        }
    }
    // INVALID VALUE
    else
    {
        printf("INVALID\n");
    }
}

// INPUT OF THE USER
long input_creditcard(void)
{
    long number;
    do
    {
        number = get_long("Give me a valid Credit Card: ");
    }
    while (number < 0 || number > 9999999999999999);
    return number;
}

// CHECKEAR LAS CIFRAS DEL NÚMERO
int count_digit(long creditcard)
{
    return (int)floor(log10(creditcard)) + 1;
}


bool credit_algorytmus(long card_number, int cifra)
{
    int checksum = 0;
    int digit = 0;
    bool alternate = false;
    while (card_number > 0)
    {
        digit = card_number % 10;

        if (alternate)
        {
           digit *= 2;
           if (digit > 9)
           {
            digit -= 9;
           }
        }

        checksum += digit;
        alternate = !alternate;
        card_number = card_number / 10;

    }

    return (checksum % 10 == 0);
}

