#include <iostream>
using namespace std;

// We want to write a function that takes in two integers and swaps their values.
// As you can see there is a right and a wrong way to go about accomplishing this.

void SwapWrong(int num1, int num2); 
void SwapCorrect(int *num1, int *num2);

// Prints the values of num1 and num2 to the screen on separate lines
void PrintNumbers(int num1, int num2);

int main()
{
	int num1 = 52;
	int num2 = 44;

	cout << "Initial values of num1 and num2" << endl;
	PrintNumbers(num1,num2);

	// This doesn't actually swap the numbers 
	SwapWrong(num1,num2);
	cout << endl << "After calling SwapWrong() on num1 and num2..." << endl;
	PrintNumbers(num1,num2);

	// This correctly swaps the numbers
	SwapCorrect(&num1,&num2);

	cout << endl << "After calling SwapCorrect() on num1 and num2..." << endl;
	PrintNumbers(num1,num2);

	return EXIT_SUCCESS;
}

void SwapWrong(int num1, int num2)
{
	// The intent of this function is to switch the values of num1 and num2.
	// Therefore, first we'll make a temporary number to store num1.
	int temp = num1;

	// Now we'll store the value of num2 into num1
	num1 = num2;

	// Finally we'll put num1's value (which is saved in temp) into num2
	num2 = temp;
}

void SwapCorrect(int *num1, int *num2)
{
	int temp = *num1;

	// Now we'll store the value of num2 into num1
	*num1 = *num2;

	// Finally we'll put num1's value (which is saved in temp) into num2
	*num2 = temp;
}

void PrintNumbers(int num1, int num2)
{
	cout << "num1 = " << num1 << endl;
	cout << "num2 = " << num2 << endl;
}