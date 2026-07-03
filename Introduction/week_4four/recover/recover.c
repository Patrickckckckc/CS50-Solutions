#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    // Check CLA's
    if (argc != 2)
    {
        printf("./recover  file_name\n");
        return 1;
    }

    // Open Memory Card
    FILE* input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Couldn´t open the File");
        return 1;
    }

    // Loop
     // Read File
    uint8_t buffer[512];
    int jpegcount = 0;
    FILE *output = NULL;

    while (fread(buffer, sizeof(uint8_t), 512, input) == 512) {
        // Look for beginning of a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Open first JPEG ( start writing the very first file)
            if (jpegcount != 0)
            {
                // CLOSE FILE
                fclose(output);
            }

            // OPEN FILE
            char new_file[20];
            sprintf(new_file, "%03i.jpg", jpegcount);
            output = fopen(new_file, "wb");
            jpegcount ++;

            // WRITE ON FILE
            fwrite(buffer, sizeof(uint8_t), 512, output);

        }

        else
        {
            // If already found JPEG
            if (output != NULL)
            {
                 fwrite(buffer, sizeof(uint8_t), 512, output);
            }
        }

    }

    // Close the last JPEG file
    if (output != NULL){
        fclose(output);
    }
    fclose(input);

}
