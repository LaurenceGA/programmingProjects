#include <iostream>
using namespace std;

void SwapWithPointers(int *num1, int *num2); 
void SwapWithReferences(int &num1, int &num2);

void PrintNumbers(int num1, int num2);

int main()
{
	int num1 = 52;
	int num2 = 44;

	cout << "Initial values of num1 and num2" << endl;
	PrintNumbers(num1,num2);

	// Some cases where a pointer could be invalid.
		//SwapWithPointers(&num1, NULL); // Crash with NULL pointer
		// SwapWithPointers(&num1, (int*)0x01234567); // Crash with valid pointer, invalid data

	// Swap the numbers with a valid pointers
	SwapWithPointers(&num1, &num2);
	cout << endl << "After calling SwapWithPointers() on num1 and num2..." << endl;
	PrintNumbers(num1,num2);

	// take the same CRASH examples from above and try them out with references.
		// SwapWithReferences(num1, NULL); // Compiler error!  A crash is avoided
		// SwapWithReferences(num1, (int*)0x01234567); // Compiler error!  A crash is avoided

	// Well what about this?
	//	 SwapWithReferences(num1, 5678); // Compiler error!  A crash is avoided

	// So as you can see by uncommenting the above function calls is that using references
	// can be safer than using pointers.
	
	// Swap the numbers again
	SwapWithReferences(num1, num2);
	cout << endl << "After calling SwapWithReferences() on num1 and num2..." << endl;
	PrintNumbers(num1,num2);

	return EXIT_SUCCESS;
}

void SwapWithPointers(int *num1, int *num2)
{
	// We'll make a temporary number to store num1
	int temp = *num1;

	// Now we'll store the value of num2 into num1
	*num1 = *num2;

	// Finally we'll put num1's value, which was saved in temp, into num2
	*num2 = temp;

}

void SwapWithReferences(int &num1, int &num2)
{
	int temp = num1; // Save off num1 into temp

	// Set num1 to num2
	num1 = num2;

	// Set num2 to num1's value stored in temp
	num2 = temp;
}

// Prints out "num1" and "num2" on separate lines
void PrintNumbers(int num1, int num2)
{
	cout << "num1 = " << num1 << endl;
	cout << "num2 = " << num2 << endl;
}