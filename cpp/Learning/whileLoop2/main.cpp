#include <iostream>
using namespace std;

int main()
{
	char letter = ' ';

	while(letter != 'w')
	{
		cout << "Enter the letter 'w': ";

		cin >> letter;
		cout << endl;
	}
	
	cout << endl << "You pressed 'w' !!!" << endl; 

	return 0;

}
	
