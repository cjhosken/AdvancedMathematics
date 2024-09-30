#include <SDL.h>
#include <SDL_image.h> // Include SDL_image for saving as PNG

#include <iostream>

int main()
{
    if(SDL_Init(SDL_INIT_VIDEO) < 0)
    {
        std::cout << "Failed to initialize the SDL2 library\n";
        return -1;
    }

    if (IMG_Init(IMG_INIT_PNG) == 0) {
        // Handle error
        return 1;
    }

    SDL_Window *window = SDL_CreateWindow("SDL2 Window",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          680, 480,
                                          0);

    if(!window)
    {
        std::cout << "Failed to create window\n";
        SDL_Quit();
        return -1;
    }

    SDL_Surface *window_surface = SDL_GetWindowSurface(window);

    if(!window_surface)
    {
        std::cout << "Failed to get the surface from the window\n";
        SDL_DestroyWindow(window);
        SDL_Quit();
        return -1;
    }

    // Define the color for the box (e.g., red)
    Uint32 box_color = SDL_MapRGB(window_surface->format, 255, 0, 0);

    // Define the rectangle (x, y, width, height)
    SDL_Rect box;
    box.x = 50;    // Top-left corner x
    box.y = 50;    // Top-left corner y
    box.w = 200;   // Width of the box
    box.h = 150;   // Height of the box

    // Fill the rectangle with the color
    SDL_FillRect(window_surface, &box, box_color);

    // Now, let's color a single pixel (e.g., green at position 300, 200)
    Uint32 pixel_color = SDL_MapRGB(window_surface->format, 0, 255, 0);

    // To directly manipulate pixels, lock the surface if needed
    if(SDL_MUSTLOCK(window_surface))
    {
        SDL_LockSurface(window_surface);
    }

    // Set a single pixel (assuming 32-bit pixels)
    Uint32 *pixels = (Uint32 *)window_surface->pixels;
    int pixel_x = 300;
    int pixel_y = 200;
    pixels[(pixel_y * window_surface->w) + pixel_x] = pixel_color;

    // Unlock the surface if it was locked
    if(SDL_MUSTLOCK(window_surface))
    {
        SDL_UnlockSurface(window_surface);
    }

    // Update the window surface to reflect changes
    SDL_UpdateWindowSurface(window);

    // Save the surface as a PNG image
    if (IMG_SavePNG(window_surface, "image.png") != 0)
    {
        std::cout << "Failed to save image as PNG: " << IMG_GetError() << "\n";
    }
    else
    {
        std::cout << "Image saved as image.png successfully!\n";
    }

    // Wait for 5 seconds
    SDL_Delay(5000);

    // Cleanup and quit
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
