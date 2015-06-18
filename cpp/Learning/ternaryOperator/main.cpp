#include <iostream>
using namespace std;

// Here are two macros that use ternary operators
#define MAX(x,y) ((x) > (y)) ? (x) : (y)
#define MIN(x,y) ((x) < (y)) ? (x) : (y)

int main()
{
	int level;

	cout << "Enter difficulty level (0 - 9): ";
	cin >> level;

	// Error check to make sure they typed in a number between (and including) 0-9
	if(level < 0 || level > 9)
	{
		cout << "You didn't follow directions did you?!?" << endl;
		return 0; // Quit the program
	}

	cout << endl << endl;

	int aiStr = (level < 5)?(level * 5):(10);

	int aiHitPts = MAX(level * 100, 500);

	// Print the variables to the screen
	cout << "AI Strengh = " << aiStr << endl;
	cout << "AI Hits Point = " << aiHitPts << endl;
	
	return 0;
}