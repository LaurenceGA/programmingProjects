#include <iostream>
using namespace std;

int main()
{
	int min=0, max=0, i;

	cout << "Number to count from: ";

	cin >> min;

	cout << "Number to count to: ";

	cin >> max;

	for (i = min; i <= max; i++)
	{
		cout << i << endl;
	}

	return 0;
}