#include <iostream>
using namespace std;

#define SHOW_ANSWERS 1

int main()
{
	int answer = 0;
	int x, y;

	if(SHOW_ANSWERS == 0)
	{
		cout << "Not showing answers now.\n";
		return 0;
	}

//************************************************************** Number 1

	answer = 8 + 8 - 16 * 2;

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 2

	answer = (2 + (2 + 2 + (4 / 2 + 2) * 2) + 2);

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 3

	answer = 60 / 15 / 2 * 2;

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 4

	answer = 10 * 10 + 10 / 10 - 10;

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 5

	answer = 10 + 10 / 10 * 10 - 10;

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 6
//******************* They are trickier from here on out :) ****

	x = 22;
	answer = x + 3 / (++x + 2);

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 7
	
	x = 5;
	y = 5;
	answer = (x + y) + (++y + ++x) / 2;

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 8

	x = 10;
	answer = x + (x + x--) + (x + x++);  // The -- (postfix decrement operator) will 
									    // decrease x's value by one (in case you didn't know)

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 9

	x = 5;
	answer = (--x + 2) + (x-- + 2) * (x + 2) - (x + 2);

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;

//************************************************************** Number 10

	y = 3;
	x = 5;
	answer = --y - (x + y) - x / 2 + (--x + 5) - y;

	if(SHOW_ANSWERS)
		cout << "The answer equals " << answer << endl << endl;


	return 0;
}