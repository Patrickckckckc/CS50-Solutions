#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // DONE IT IN FILTER_LESS
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // DONE IT IN FILTER_LESS
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // DONE IT IN FILTER_LESS
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy
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

    // Define Gx and Gy
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int row = 0; row < height; row++)
    {
        for (int column = 0; column < width; column++)
        {
            // INSIDE ONE PIXEL
            // Look at the 9 pixels around them
            // Declare Variables
            double totalgx_red = 0;
            double totalgx_green = 0;
            double totalgx_blue = 0;
            double totalgy_red = 0;
            double totalgy_green = 0;
            double totalgy_blue = 0;
            int rn_og = row - 1;
            int cn_og = column - 1;
            for (int rn = row - 1; rn <= row + 1; rn++)
            {
                for (int cn = column - 1; cn <= column + 1; cn++)
                {
                    // Check with just pixels inside
                    if (rn < 0 || rn >= height || cn < 0 || cn >= width)
                    {
                        continue;
                    }
                    // Take gx value starting 0 in the middle  red, green, value
                    totalgx_red += gx[rn - rn_og][cn - cn_og] * copy_image[rn][cn].rgbtRed;
                    totalgx_green += gx[rn - rn_og][cn - cn_og] * copy_image[rn][cn].rgbtGreen;
                    totalgx_blue += gx[rn - rn_og][cn - cn_og] * copy_image[rn][cn].rgbtBlue;

                    // gy
                    totalgy_red += gy[rn - rn_og][cn - cn_og] * copy_image[rn][cn].rgbtRed;
                    totalgy_green += gy[rn - rn_og][cn - cn_og] * copy_image[rn][cn].rgbtGreen;
                    totalgy_blue += gy[rn - rn_og][cn - cn_og] * copy_image[rn][cn].rgbtBlue;
                }
            }

            // Compute each new value of square root gx*gx + gy*gy for red, green, value, just less
            // than 255
            double gxgyred = round(sqrt((pow(totalgx_red, 2.0) + pow(totalgy_red, 2.0))));
            if (gxgyred > 255)
            {
                gxgyred = 255;
            }
            double gxgygreen = round(sqrt((pow(totalgx_green, 2.0) + pow(totalgy_green, 2.0))));
            if (gxgygreen > 255)
            {
                gxgygreen = 255;
            }
            double gxgyblue = round(sqrt((pow(totalgx_blue, 2.0) + pow(totalgy_blue, 2.0))));
            if (gxgyblue > 255)
            {
                gxgyblue = 255;
            }

            image[row][column].rgbtRed = gxgyred;
            image[row][column].rgbtGreen = gxgygreen;
            image[row][column].rgbtBlue = gxgyblue;
        }
    }
    return;
}
