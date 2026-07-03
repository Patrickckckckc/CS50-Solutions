#include <cs50.h>
#include <stdio.h>

int input_money(void);

int main(void)
{
    // ASK FOR INPUT (AMOUNT OF MONEY IN CENTS)
    int cash = input_money();

    // DEFINE VARIABLES
    int quarter;
    int dime;
    int nickel;
    int penny;
    int total;
    // CALCULATE QUARTER (25)
    quarter = cash / 25;
    cash = cash % 25;
    // CALCULATE DIME (10)
    dime = cash / 10;
    cash = cash % 10;
    // CALCULATE NICKEL (5)
    nickel = cash / 5;
    cash = cash % 5;
    // CALCULATE PENNY (1)
    penny = cash;

    // PRINT ANSWER
    total = quarter + dime + nickel + penny;

    printf("The total of coins is: %i \n", total);
}

int input_money(void)
{
    int money;
    do
    {
        money = get_int("How much it is?(In cents) ");
    }
    while (money < 0);
    return money;
}
