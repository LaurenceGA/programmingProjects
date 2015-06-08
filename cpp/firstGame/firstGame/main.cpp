#include "SDL/SDL.h"
#include <iostream>

using namespace std;

int main(int argC, char *args[]) {
    const int SCREEN_WIDTH = 1280;
    const int SCREEN_HEIGHT = 960;
    const int SCREEN_BITS = 32;

    // Start SDL
    SDL_Init(SDL_INIT_EVERYTHING);
    cout << "SDL started" << endl;

    SDL_Surface* hello = NULL;
    SDL_Surface* screen = NULL;

    // Set up screen
    screen = SDL_SetVideoMode(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BITS, SDL_SWSURFACE);

    // Load image
    hello = SDL_LoadBMP("hello.bmp");

    // Apply image to screen
    SDL_BlitSurface(hello, NULL, screen, NULL);

    // Update screen
    SDL_Flip(screen);

    // Pause
    SDL_Delay(2000);

    // Free loaded image
    SDL_FreeSurface(hello);

    // Quit SDL
    SDL_Quit();
    cout << "SDL quit" << endl;

    return 0;
}
