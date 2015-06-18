#include <iostream>
using namespace std;

void IncreaseNumber(int Number);
void IncreaseNumber2(int *pNumber);

void IncreaseNumber(int Number)
{
	Number += 5;
}

void IncreaseNumber2(int *pNumber)
{
	*pNumber += 5;
}

int main()
{														
	int num = 0;

	IncreaseNumber(num);

	cout << "Num now equals: " << num << endl << endl;

	IncreaseNumber2(&num);
															
	cout << "Num now equals: " << num << endl << endl;
	return 0;
}