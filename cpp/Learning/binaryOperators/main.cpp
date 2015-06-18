/*
AND (&)
OR  (|)
XOR "exclusive or" (^)

	101 = 5
	110 = 6

	The AND operation:	0 AND 0 equals 0
						0 AND 1 equals 0
						1 AND 0 equals 0
						1 AND 1 equals 1

	101
	110	 AND
	--- 
	100 = 4				So 5 & 6 = 4

	************************************************************************************************

	The OR operator

	The OR operation:   0 OR 0 equals 0
						0 OR 1 equals 1
						1 OR 0 equals 1
						1 OR 1 equals 1

	101
	110  OR
	---
	111 = 7

	************************************************************************************************

	The XOR (exclusive or) operator

	The XOR operation:	0 XOR 0 equals 0
						0 XOR 1 equals 1
						1 XOR 0 equals 1
						1 XOR 1 equals 0

	101
	110  XOR
	---
	011 = 3		So 5 ^ 6 = 3


if(a_number & 1)
	// The number is odd
else
	// The number is even

Truth table --

AND	 OR	 XOR
00|  0    0   0
-------------------
01|  0    1   1
-------------------
10|  0    1   1
-------------------
11|  1    1   0
-------------------

*/

#define SHOW_ANSWERS 1

#include <iostream>
using namespace std;

int main()
{
	int num1 = 8;
	int num2 = 3;

	int answer = 6;

	// Print out the result of num1 AND num2
	answer = num1 & num2;
	
	if(SHOW_ANSWERS)
		cout << num1 << " & " << num2 << " = " << answer << endl << endl;
	
	// Print out the result of num1 OR num2
	answer = num1 | num2;

	if(SHOW_ANSWERS)
		cout << num1 << " | " << num2 << " = " << answer << endl << endl;

	// Print out the result of num1 XOR num2
	answer = num1 ^ num2;

	if(SHOW_ANSWERS)
		cout << num1 << " ^ " << num2 << " = " << answer << endl << endl;

	// Print out the result of (num1 AND num2) XOR (num1 OR num2)
	answer = (num1 & num2) ^ (num1 | num2);

	if(SHOW_ANSWERS)
		cout << "(" << num1 << " & " << num2 << ") ^ (" << num1 << " | " << num2
			 << ") = " << answer << endl;

		return 0;

}