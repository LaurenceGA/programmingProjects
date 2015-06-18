#include <conio.h> // So we can use _kbhit()
#include <iostream>
using namespace std;

int main()
{
	do
	{
		cout << "Still in the do...while loop" << endl;
	
	} while(!_kbhit());

	return EXIT_SUCCESS;
}