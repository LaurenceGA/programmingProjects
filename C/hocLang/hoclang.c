#include <stdio.h>
#include <stdbool.h>

#include "headers/lexer.h"

int main(int argc, char *argv[]) {
	FILE *inFile = NULL;
	bool fromInp = false;

	if (argc == 1) {
		// Get stdin
		inFile = stdin;
		fromInp = true;
	} else if (argc == 2) {
		// From argv[1]
		inFile = fopen(argv[1], "r");

	}

	Lexer *lexer = newLexer(inFile);

	

	if (!fromInp) {
		fclose(inFile);
	}

	freeLexer(lexer);

	return 0;
}
