#include <windows.h> // We include this header file so we can call the function GetTickCount()
#include <iostream>
using namespace std;

int main()
{
	int num1 = rand(); //returns an integer between 0 and RAND_MAX (32767)

	cout << "A call to rand() gave us: " << num1 << endl;

	num1 = rand()%15; // Here num1 will equal a number between (and including) 0 - 14

	cout << endl << "rand()%15 = " << num1 << endl;

	num1 = rand()%35; // (0 - 34)

	cout << endl << "rand()%35 = " << num1 << endl;

	srand(GetTickCount());	// Could also use time(NULL)

	num1 = rand()%100;

	cout << endl << "rand()%100 = " << num1 << endl;

	return 0;
}