#include <iostream>
using namespace std;

int main()
{
	int number = 0;
	char ch = 0;

	cout << "Input a number between 1 and 3: ";																					
	cin >> number;

	switch(number)
	{
		case 1:
			cout << "You typed in the number 1!\n";
			break;

		case 2:
			cout << "You typed in the number 2!\n";	
			break;

		case 3:
			cout << "You typed in the number 3!\n";
			break;
									
		default:
			cout << "You didn't follow directions!\n";
			break;
	}

	cout << "\n\nInput a character: ";																	
	cin >> ch;

	switch(ch)
	{
		case 'a':
			cout << "You typed in an A!\n";
			break;

		case 'b':
			cout << "You typed in a B!\n";	
			break;

		case 'c':
			cout << "You typed in a C!\n";
			break;
									
		default:
			cout << "You did not type an a, b or c!\n";
			break;										
	}

	cout << "\n\nInput a lowercase or uppercase character: ";		
	cin >> ch;

	switch(ch)
	{
		case 'a': case 'A':
			cout << "You typed in an A!\n";
			break;

		case 'b': case 'B':
			cout << "You typed in a B!\n";	
			break;

		case 'c': case 'C':
			cout << "You typed in a C!\n";
			break;
									
		default:
			cout << "You did not type an a, b or c!\n";
			break;										
	}										
	
	return 0;
}