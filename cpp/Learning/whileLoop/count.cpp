#include <iostream>
using namespace std;

int main()
{
	int min = 0, max = 0, i = 0;

	cout << "Number to count from: ";

	cin >> min;

	cout << "Number to count to: ";

	cin >> max;

	while (min <= max)
	{
		cout << min << endl;
		min++;
	}

	return 0;
}