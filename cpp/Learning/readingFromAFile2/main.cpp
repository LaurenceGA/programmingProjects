#include <iostream>
#include <string>
#include <fstream> 

using namespace std;

int main()
{
	ifstream fileIn("GT.txt");	// ifstream constructor

	// Error Check
	if(!fileIn)
		return 1;

	string strBuff;

	int i = 0;

	while(true)
	{
		fileIn >> strBuff;
		if(fileIn.eof()) break;

		cout << strBuff << " ";
	}

	cout << endl;

	fileIn.close();
		return 0;
}