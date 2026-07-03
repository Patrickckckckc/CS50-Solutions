#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string encipher_text(string text, int key);
int main(int argc, string argv[])
{
    // GET KEY
        // Check if is just one argument
            if (argc != 2)
                {
                        printf("Usage: ./caesar key\n");
                                return 1;
                                    }
                                        // Check if is numeric
                                            for (int i = 0, length = strlen(argv[1]); i < length; i++)
                                                {
                                                        if (!isdigit(argv[1][i]))
                                                                {
                                                                            printf("Usage: ./caesar key\n");
                                                                                        return 2;
                                                                                                }
                                                                                                    }
                                                                                                        // Convert key string into key int
                                                                                                            int key = atoi(argv[1]);

                                                                                                                // GET PLAINTEXT
                                                                                                                    string plain_text = get_string("Text: ");

                                                                                                                        // ENCIPHER
                                                                                                                            string cipher_text = encipher_text(plain_text, key);

                                                                                                                                // Print ciphertext
                                                                                                                                    printf("Ciphertext: %s\n", cipher_text);
                                                                                                                                    }

                                                                                                                                    // CHANGE THE PLAINTEXT INTO CIPHERTEXT
                                                                                                                                    string encipher_text(string text, int key)
                                                                                                                                    {
                                                                                                                                        for (int i = 0, length = strlen(text); i < length; i++)
                                                                                                                                            {
                                                                                                                                                    // Check Alphabetical
                                                                                                                                                            if (isalpha(text[i]))
                                                                                                                                                                    {
                                                                                                                                                                                // Check the case
                                                                                                                                                                                            if (isupper(text[i]))
                                                                                                                                                                                                        {
                                                                                                                                                                                                                        int plain_letter = text[i] - 'A';
                                                                                                                                                                                                                                        int cipher_letter = (plain_letter + key) % 26;
                                                                                                                                                                                                                                                        text[i] = cipher_letter + 'A';
                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                else
                                                                                                                                                                                                                                                                                            {
                                                                                                                                                                                                                                                                                                            int plain_letter = text[i] - 'a';
                                                                                                                                                                                                                                                                                                                            int cipher_letter = (plain_letter + key) % 26;
                                                                                                                                                                                                                                                                                                                                            text[i] = cipher_letter + 'a';
                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                                                                                                                                        return text;
                                                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                                        