#include <iostream>
#include <windows.h>
#include <time.h>
using namespace std;

#define MAX_NUMBERS 15

#define PRINT_NUM(num) cout << num << endl

int main()
{
	int list[MAX_NUMBERS]={0}, i=0;

	cout << "\nThe not so random list:\n\n";

	for(i=0; i < MAX_NUMBERS; i++)			// We call our for loop that will continue to print out MAX_NUMBERS (15) random numbers
	{										// Start the cycle if the expression in the middle is true.
		list[i] = rand();					// list[i] means, the slot "i" (which will start out as 0) in list gets a random number.
											// Say, the random number came out to be 2200.  In the beginning, since i = 0;  list[0] would equal 2200;
		PRINT_NUM(list[i]);					// If list[i] was 2200 , then PRINT_NUM() would print out 2200 to the screen.	
	}										// End of the cycle and check at the top if we need to continue.
		
											// The for loop will continue to go until i == 15.  Then it will stop.
											// Run this program again and you will notice that the numbers are the same every time.
	cout << "\nThe TRULY random list:\n\n";	// They are different from each other, but the same every time.
											// We need to "seed" the random number generator. To do this, we use time.
											// The computer's internal clock will always be changing, so we start the random number on our system's time.
	srand( (unsigned int)time(NULL) );		// srand() stands for "seed randomizer"  ... or something like that :)
											// We pass the function time() to srand() to seed the random generator. We pass in NULL to time() because we
											// don't care what format is returned.  However, we need to cast the return value to an unsigned int because
											// that is what srand() wants!

	Sleep(3000);							// This functions causes a delay for about 3 seconds.  1000 is ~ 1 second.  ~ means approximately. (1000 Milliseconds = 1 second)

											// Let's see that again...
	for(i=0; i < MAX_NUMBERS; i++)			// Now you'll notice the differences in numbers EVERY TIME .. or at least when the clock changes :)
	{											
		list[i] = rand();					// Randomize the new list
											
		PRINT_NUM(list[i]);					// Print out the randomized number.									
	}
											// Now we will restrict the random numbers so that we don't get numbers in the 10's of thousands.
											// Print the new title of numbers
	cout << "\nThe *restricted* TRULY random list:\n\n";

	Sleep(3000);							// Sleep for 3 seconds

	for(i=0; i < MAX_NUMBERS; i++)			// Notice the differences in numbers every time.
	{											
		list[i] = rand() % 100;				// Randomize the new list with numbers less than 100.
											// using the modulus operator "%" we can restrict the random numbers to being less than 100;
											// Here is an example on how modulus works.  It's kind of like divide, except it returns the remainder of the divide instead
											// "  15 % 5 = 0,      15 % 7 = 1,    15 % 26 = 15 "
											// Can you see why?  it's the remainder.  15 / 5 = 3 with NO remainder, so 15 % 5 = 0
											// 15 / 7 has a remainder of 1.  15 % 26 returns 15 because anything being moded by a higher number, just returns that number that is being moded.
											
		PRINT_NUM(list[i]);					// Print out the randomized number.									
	}
	
	return 0;								// Return zero for "zero problems in this program"
}											// The end of the program

// *FUNCTIONS EXPLANATION*
//
// Let's talk about the Sleep() function for a second.  Sleep() is a function that does a delay.
// In the case of Sleep(), you want to tell it how long to delay...  So, we pass in the 
// number 3000 like so:  Sleep(3000);  Sleep takes milliseconds as the parameter.  1000 = 1 second.
// I would like to caution you on how you use your macros.  They can be very nice, but also
// can cause problems if you don't do them correctly.  Make sure you know the macro compiles
// correctly before you start adding it all over your project.  This will save time with debugging
// in case you didn't have the syntax right in the first place.

// © 2000-2005 GameTutorials
