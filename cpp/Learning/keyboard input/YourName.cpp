#include <iostream>				// Standard C++ definitions
#include <string>				// String definitions

using namespace std;
												

int main()
{
	string strName;

	cout << "What is your name? ";

	cin >> strName;

	cout << "Hello " << strName << endl;
	
	return 0;
}