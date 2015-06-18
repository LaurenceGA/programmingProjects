#include <iostream>
using namespace std;

int main()
{
	char name[] = "Carlos";

	cout << "name[] length = " << strlen(name) << endl << endl << endl;

	//cout << name << endl;
	//cout << name[2] << endl << endl;

	name[3] = name[2];

	//cout << name << endl << endl;

	name[5] = 't';

	//cout << name << endl << endl;

	name[3] = NULL;

	//cout << name << endl << endl;


	// Array of type int

	int numbers[] = {0,1,2,3,4,5,6,7,8,9};

	cout << "numbers[2] = " << numbers[2] << endl;
	
	//cout << numbers << endl;



	return EXIT_SUCCESS;

}