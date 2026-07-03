#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

const int alphabet_points[] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                               1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int score_calculator(string word);
int main(void)
{
    // Prompt the user for two words
    string first_word = get_string("PLAYER 1: ");
    string second_word = get_string("PLAYER 2: ");

    // Compute the score of each word
    int first_points = score_calculator(first_word);
    int second_points = score_calculator(second_word);

    // Print the winner
    if (first_points > second_points)
    {
        printf("Player 1 wins!\n");
    }
    else if (first_points < second_points)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int score_calculator(string word)
{
    int score = 0;
    for (int i = 0, length = strlen(word); i < length; i++)
    {
        if (isalpha(word[i])) // is alphabetical
        {
            // change Upper Case
            word[i] = toupper(word[i]);
            // Calculate the puntaje with the array of alphabet
            int point = word[i] - 'A';
            // Aumentar el score
            score += alphabet_points[point];
        }
    }
    return score;
}
