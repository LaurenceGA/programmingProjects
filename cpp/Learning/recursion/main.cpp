#include <iostream>
using namespace std;

typedef unsigned int uint;

uint Factorial(uint num);

int main()
{
	cout << Factorial(3) << endl;
		return 0;
}

uint Factorial(uint num)
{
	if (num == 1)
		return 1;

	else
		return num * Factorial(num - 1);
}