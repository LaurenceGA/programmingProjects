#include <iostream>
using namespace std;

int Power(int base, int exp);

int main()
{

	int result = 0;

	result = Power(2,3);

	cout << "2 raised to the 3rd power = " << result << endl;

	result = Power(5,3);

	cout << "5 raised to the 3rd power = " << result << endl;

	Power(4,4);

	cout << "4 raised to the 6th power = " << Power(4,6) << endl;
	return 0;

}

int Power(int base, int exp)
{
	int result = 1;

	while(exp--)
		result *= base;

	return result;

}