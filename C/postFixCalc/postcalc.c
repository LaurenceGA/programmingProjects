#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

#include "headers/stack.h"
#include "headers/vector.h"

#define BUFFSIZE 16

/* A calculator that takes a post fix expression and evaluates it */
int main(int argc, char *argv[]) {
	/* If no argument is given, then expression input is from stdin, otherwise from arguments */
	char **tokenArray = argv;
	Vector *inpVect = newVector();
	bool fromInp = false;
	int counter = argc;

	if (argc == 1) {
		fromInp = true;
		
		char buff[BUFFSIZE];
		while (scanf("%s", buff) != EOF) {
			char *str = (char *) malloc(sizeof(char) * strlen(buff) + 1);
			strcpy(str, buff);
			append(inpVect, str);
			if (scanf("*\n") != EOF) {
				break;
			}
		}

		tokenArray = (char **)inpVect->data;
		counter = inpVect->size + 2;
	}

	double v1, v2;
	NumStack *valStack = newStack();
	
	int ind = (fromInp) ? 0: 1;
	while (--counter > 0) {
		printf("\n%s\n", "HERE");

		//char *token = *++tokenArray;	// Grab the token
		char *token = (tokenArray)[ind];
		ind += 1;
		if (strlen(token) == 1 && ispunct(*token)) {	// If it's an operator
			switch (*token) {
				case '+':
					push(valStack, pop(valStack) + pop(valStack));
				break;

				case '-':
					// Subtraction is associative, so values must be popped first
					v1 = pop(valStack);
					v2 = pop(valStack);
					push(valStack, v2 - v1);
				break;

				case '*':
					push(valStack, pop(valStack) * pop(valStack));
				break;

				case '/':
					// Division is associative, so values must be popped first
					v1 = pop(valStack);
					v2 = pop(valStack);
					push(valStack, v2 / v1);
				break;

				case '^':
					// Exponentiation is associative, so values must be popped first
					v1 = pop(valStack);
					v2 = pop(valStack);
					push(valStack, pow(v2, v1));
				break;

				default:
					fprintf(stderr, "Unknown token %c", *token);
				break;
			}
		} else {	// Must be a number
			push(valStack, atof(token));
		}
	}

	double finalVal = pop(valStack);

	if (!isEmpty(valStack)) {
		fprintf(stderr, "%s\n\n%s\n", "Bad input!",
				"Put whitespace between arguments.\nEscape '*'.");
		return 1;
	}

	printf("%sAnswer: %g\n", (fromInp) ? "\n" : "", finalVal);

	if (fromInp) {
		for (int i=0; i < inpVect->size; i++) {
			free((char *)inpVect->data[i]);
		}
		freeVector(inpVect);
	}
	freeStack(valStack);

	return 0;
}
