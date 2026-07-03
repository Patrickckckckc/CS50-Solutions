#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            // Take the average
            double average = round((image[row][column].rgbtBlue + image[row][column].rgbtGreen +
                                    image[row][column].rgbtRed) /
                                   3.0);
            // Change values
            image[row][column].rgbtBlue = average;
            image[row][column].rgbtGreen = average;
            image[row][column].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia

void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            // Original values
            int og_red   = image[row][column].rgbtRed;
            int og_green = image[row][column].rgbtGreen;
            int og_blue  = image[row][column].rgbtBlue;

            // Apply sepia formula
            int newRed   = (int)round(0.393 * og_red + 0.769 * og_green + 0.189 * og_blue);
            int newGreen = (int)round(0.349 * og_red + 0.686 * og_green + 0.168 * og_blue);
            int newBlue  = (int)round(0.272 * og_red + 0.534 * og_green + 0.131 * og_blue);

            // Clamp values to 255
            if (newRed > 255)   newRed = 255;
            if (newGreen > 255) newGreen = 255;
            if (newBlue > 255)  newBlue = 255;

            // Assign back to image
            image[row][column].rgbtRed   = (uint8_t)newRed;
            image[row][column].rgbtGreen = (uint8_t)newGreen;
            image[row][column].rgbtBlue  = (uint8_t)newBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a Copy of image
    RGBTRIPLE copy_image[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            copy_image[row][column].rgbtRed = image[row][column].rgbtRed;
            copy_image[row][column].rgbtGreen = image[row][column].rgbtGreen;
            copy_image[row][column].rgbtBlue = image[row][column].rgbtBlue;
        }
    }

    for (int row = 0; row < height; row++)
    {
        // Swap pixels horizontal
        for (int column = 0; column < width; column++)
        {
            image[row][column].rgbtBlue = copy_image[row][width - column - 1].rgbtBlue;
            image[row][column].rgbtGreen = copy_image[row][width - column - 1].rgbtGreen;
            image[row][column].rgbtRed = copy_image[row][width - column - 1].rgbtRed;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy of the original image
    RGBTRIPLE copy_image[height][width];
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            copy_image[row][column] = image[row][column];
        }
    }

    // Apply blur
    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            int total_red = 0;
            int total_green = 0;
            int total_blue = 0;
            int total_around = 0;

            // Loop through neighboring pixels (3x3 box)
            for (int rn = row - 1; rn <= row + 1; rn++)
            {
                for (int cn = column - 1; cn <= column + 1; cn++)
                {
                    // Skip out-of-bound indices
                    if (rn < 0 || rn >= height || cn < 0 || cn >= width)
                    {
                        continue;
                    }

                    total_red   += copy_image[rn][cn].rgbtRed;
                    total_green += copy_image[rn][cn].rgbtGreen;
                    total_blue  += copy_image[rn][cn].rgbtBlue;
                    total_around++;
                }
            }

            // Compute averages (rounded to nearest int)
            int average_red   = (int)round((double)total_red / total_around);
            int average_green = (int)round((double)total_green / total_around);
            int average_blue  = (int)round((double)total_blue / total_around);

            // Assign blurred values back to image
            image[row][column].rgbtRed   = (uint8_t)average_red;
            image[row][column].rgbtGreen = (uint8_t)average_green;
            image[row][column].rgbtBlue  = (uint8_t)average_blue;
        }
    }
}
