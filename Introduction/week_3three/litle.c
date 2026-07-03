#include <cs50.h>
#include <stdio.h>

int collatz(int coll);

int main(void)
{
  int number;
  do
  {
     number = get_int("Give me a positive number: ");
  }
  while (number < 1);
  int step_count = collatz(number);
  printf("%i\n ", step_count);
}

int collatz(int coll)
{
    if (coll == 1)
    {
        return 0;
    }
    else if (coll % 2 == 0)
    {
        return 1 + collatz(coll/2);
    }
    else
    {
        return 1 + collatz(coll - 1);
    }
    // base
}
