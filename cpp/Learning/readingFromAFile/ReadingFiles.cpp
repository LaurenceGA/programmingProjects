#include <iostream>
#include <string>
#include <fstream>	// Access file streams
using namespace std;

int main()
{
	ifstream fin;
	string strLine = "";
	string strWord = "";
	string strName = "";
	int health=0, gold = 0;
														
	fin.open("Stats.txt");													
														
	if(fin.fail())
	{
		cout << "ERROR: Could not find Stats.txt!\n";

		return 1;
	}
														
	cout << endl;

	while(fin >> strWord)
		cout << strWord;

	cout << endl << endl;
														
	fin.clear();
	fin.seekg(NULL, ios::beg);
														

	while(getline(fin, strLine))
		cout << strLine << endl;
	
	cout << endl;


	fin.clear();
	fin.seekg(NULL, ios::beg);


	fin >> strWord >> strName;
	fin >> strWord >> health;
	fin >> strWord >> gold;

	cout << "The Player's name is:     " << strName << endl;
	cout << "The Player's health is:   " << health << endl;
	cout << "The Player's gold is:     " << gold << endl;

	fin.close();

	return 0;
}