#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ofstream fout;

	string szLine = "";
	string szWord = "";
	string szName = "Adol";
	int health = 100, gold = 75;

	fout.open("Stats.txt");

	fout << "Player: " << szName << endl;
	fout << "Health: " << health << endl;
	fout << "Gold: " << gold << endl;


	fout.close();

	return 0;
}