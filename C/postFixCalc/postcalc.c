#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

#include "headers/stack.h"
#include "headers/vector.h"

#define BUFFINIT 1

/* A calculator that takes a post fix expression and evaluates it */
int main(int argc, char *argv[]) {
	/* If no argument is given, then expression input is from stdin, otherwise from arguments */
	char **tokenArray = argv;
	Vector *inpVect = newVector();
	bool fromInp = false;
	int counter = argc;

	if (argc == 1) {
		fromInp = true;
		
		printf("%s\n\n>", "Enter equation:");

		char *buff = (char *) malloc(sizeof(char) * BUFFINIT + 1);
		char c;
		int buffInd = 0, buffsize = BUFFINIT;
		while ((c = getchar()) != EOF) {
			if (c == ' ' || c == '\n') {
				buff[buffInd] = '\0';
				buffInd = 0;
				char *str = (char *) malloc(sizeof(char) * strlen(buff) + 1);
				strcpy(str, buff);
				append(inpVect, str);
				if (c == '\n')
					break;
			} else {
				if (buffInd > buffsize-1) {
					buffsize *= 2;
					buff = realloc(buff, sizeof(char) * buffsize + 1);
				}
				buff[buffInd++] = c;
			}
		}

		tokenArray = (char **)inpVect->data;
		counter = inpVect->size + 1;
		free(buff);
	}

	double v1, v2;
	NumStack *valStack = newStack();

	int ind = (fromInp) ? 0: 1;
	while (--counter > 0) {
		char *token = (tokenArray)[ind++];

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
					fprintf(stderr, "Unknown token %c\n", *token);
				break;
			}
		} else {	// Must be a number
			push(valStack, atof(token));
		}
	}

	double finalVal = pop(valStack);

	if (!isEmpty(valStack)) {
		fprintf(stderr, "%s\n\n%s\n", "Bad input!",
				(!fromInp) ? "Put whitespace between arguments.\nEscape '*'." : "\n");
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
