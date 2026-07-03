#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int Alphabectical_Letters = 26;
string substitution_text(string text, string key);
int main(int argc, string argv[])
{
    // GET KEY
    // If is not 2 arguments
    if (argc != 2)
    {
        printf("./sus KEY\n");
        return 1;
    }
    // If they are not 26 chats
    else if (strlen(argv[1]) != Alphabectical_Letters)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    // If is not alphabetical
    for (int i = 0; i < Alphabectical_Letters; i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Key must only contain alphabetical characters.\n");
            return 1;
        }
    }

    bool letter_use[26] = {false};
    // Check what characteres there are
    for (int i = 0; i < Alphabectical_Letters; i++)
    {
        int number_letter = toupper(argv[1][i]) - 'A';
        if (letter_use[number_letter])
        {
            // Ya estaba marcada → repetida
            printf("Key must not contain repeated characters.\n");
            return 1;
        }
        letter_use[number_letter] = true;
    }
    for (int i = 0; i < Alphabectical_Letters; i++)
    {
        if (letter_use[i] == false)
        {
            printf("Key must not contain repetitive characters.\n");
        }
    }

    // GET PLAINTEXT
    string plain_text = get_string("Text: ");

    // SUBSTITUTION FUNCTION
    string cipher_text = substitution_text(plain_text, argv[1]);

    // PRINT CIPHERTEXT
    printf("Ciphertext: %s\n", cipher_text);
}

// SUBSTITUTION FUNCTION, reuse
string substitution_text(string text, string key)
{
    // Check Alphabetical, Good but change the case
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        if (isalpha(text[i]))
        {
            // Check the case
            if (isupper(text[i]))
            {
                int plain_letter = text[i] - 'A';
                text[i] = key[plain_letter];
            }
            else
            {
                int plain_letter = text[i] - 'a';
                text[i] = key[plain_letter];
                text[i] = tolower(text[i]);
            }
        }
    }
    return text;
}
