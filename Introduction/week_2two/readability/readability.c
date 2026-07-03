#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string word);
int count_words(string word);
int count_sentences(string word);
int main(void)
{
    // Prompt the user for some text
    const string text = get_string("Text: ");
    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Compute the Coleman-Liau index
    float L = (float) letters * 100 / words;
    float S = (float) sentences * 100 / words;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade_level = round(index);

    // Print the grade level
    if (grade_level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade_level >= 1 && grade_level < 16)
    {
        printf("Grade %i\n", grade_level);
    }
    else if (grade_level >= 16)
    {
        printf("Grade 16+\n");
    }
}

// # Letters
int count_letters(string word)
{
    int total_letters = 0;
    for (int i = 0, length = strlen(word); i < length; i++) // Iterate in all the symbols
    {
        if (isalpha(word[i]))
        {
            total_letters++;
        }
    }
    return total_letters;
}

// # Words
int count_words(string word)
{
    int total_words = 1;
    for (int i = 0, length = strlen(word); i < length; i++) // Iterate in all the symbols
    {
        if (isblank(word[i]))
        {
            total_words++;
        }
    }
    return total_words;
}

// # Sentences
int count_sentences(string word)
{
    int total_sentences = 0;
    for (int i = 0, length = strlen(word); i < length; i++) // Iterate in all the symbols
    {
        if (word[i] == '.' || word[i] == '?' || word[i] == '!')
        {
            total_sentences++;
        }
    }
    return total_sentences;
}
