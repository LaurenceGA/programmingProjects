#include <iostream>
#include <string>							// This allows us to use the variable type, "string"
using namespace std;

int main()
{
	string strAnswer = "";

	cout << "Do you like programming yet? ";

	cin >> strAnswer;

	if( ( strAnswer == "yes" ) || ( strAnswer == "Yes" ))
	{
		cout << "Good." << endl;	
	}
	else
	{
		cout << "Too bad." << endl;
	}								
	
	cout << "Do you like programming yet? " << endl;

	cin >> strAnswer;

	if( ( strAnswer[0] == 'y' ) || ( strAnswer[0] == 'Y' ) )
	{
		cout << "Good." << endl;
	}
	else
	{									
		cout << "Too bad." << endl;
	}
											
	return 0;
}