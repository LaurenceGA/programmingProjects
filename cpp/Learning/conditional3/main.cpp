#include <iostream>	// So we can use "cout"
using namespace std;

int main()
{
	int num1 = 20;
	int num2 = 0;

	if(num1 && num2)
		cout << num1 << " AND " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " AND " << num2 << " is a false statement" << endl << endl;

	if(num1 || num2)
		cout << num1 << " OR " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " OR " << num2 << " is a false statement" << endl << endl;

	if(!num1)
		cout << "NOT " << num1 << " is a true statement" << endl << endl;
	else
		cout << "NOT " << num1 << " is a false statement" << endl << endl;

	if(num1 == num2)
		cout << num1 << " EQUALS " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " EQUALS " << num2 << " is a false statement" << endl << endl;

	if(num1 < num2)
		cout << num1 << " is LESS THAN " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " is LESS THAN " << num2 << " is a false statement" << endl << endl;

	if(num1 > num2)
		cout << num1 << " is GREATER THAN " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " is GREATER THAN " << num2 << " is a false statement" << endl << endl;

	if(num1 <= num2)
		cout << num1 << " is LESS THAN OR EQUAL TO " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " is LESS THAN OR EQUAL TO " << num2 << " is a false statement" << endl << endl;

	if(num1 >= num2)
		cout << num1 << " is GREATER THAN OR EQUAL TO " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " is GREATER THAN OR EQUAL TO " << num2 << " is a false statement" << endl << endl;

	if(num1 != num2)
		cout << num1 << " DOES NOT EQUAL " << num2 << " is a true statement" << endl << endl;
	else
		cout << num1 << " DOES NOT EQUAL " << num2 << " is a false statement" << endl << endl;

	return EXIT_SUCCESS;	// Program ended successfully
}

/* 
	Okay you now hopefully have the LOGIC CONDITIONAL STATEMENTS (operators) down pat %)

	But if you're still having trouble, post a message on the GT message board
	at www.GameTutorials.com.
*/
	
/*-------------------------*\
|  Programmed by:  TheTutor	|
|  ©2006 GameTutorials, LLC	|
\*-------------------------*/