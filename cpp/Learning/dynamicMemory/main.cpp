#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	// Creates a "file stream" to the text file "TheTextFile.txt"
	ifstream fileIn("TheTextFile.txt"); 

	// Error check -- If "TheTextFile.txt" doesn't exist (or isn't this directory)
	//				  fileIn will equal NULL -- So we check that fileIn DOES NOT equal NULL.
	if(!fileIn)
		return EXIT_FAILURE;

	int count = 0;
	char dummyChar;

	while(!fileIn.eof()) // Keep going until the we've reached the END-OF-THE-FILE
	{
		fileIn >> dummyChar; // Read in the file character by character
		count++; // We've read another character
	}

	cout << "There are " << count << " characters in \"TheTextFile.txt\"" << endl;

	char *letters = new char[count];

	fileIn.clear();
	fileIn.seekg(NULL,ios::beg);

	count = 0;

	while(!fileIn.eof())
	{
		fileIn >> letters[count];
		count++; // Move to next index
	}

	letters[count - 1] = NULL;

	// Display all the characters in the array
	cout << endl << endl << letters << endl;

	delete[] letters;

	fileIn.close();
		return EXIT_SUCCESS;

}