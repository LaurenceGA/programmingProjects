#include <iostream>
using namespace std;

int main()
{
	int age=0;

	cout << "How old are you? ";

	cin >> age;
											
	if (age > 20)
	{
		cout << "You're over 20 huh?" << endl;
	}

	if(age > 30)
		cout << "You're over 30!?" << endl;

	if(age < 20)
	{
		cout << "You're a young'n!" << endl;
	}
				
	if (age < 20 && age > 12)
	{
		cout << "Being in your teens can be tough..." << endl;
	}
	
	if(age == 100)
		cout << "WOW!  What's your secret!?" << endl;
	
	if(age > 50)
		cout << "Life after 50 can be great!" << endl;
	else
		cout << "You've still got a LONG way to go..." << endl;

	return 0;
}