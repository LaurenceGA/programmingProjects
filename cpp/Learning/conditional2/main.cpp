#include <iostream>
using namespace std;

int main()
{
	int num;

	cout << "Enter a number: ";

	cin >> num;

	if(num > 0)
	{
		cout << "num is positive" << endl << endl;
	}
	else if(num < 0)
	{
		cout << "num is negative" << endl << endl;
	}
	else
	{
		cout << "num equals zero" << endl << endl;
	}

	return 0;
}