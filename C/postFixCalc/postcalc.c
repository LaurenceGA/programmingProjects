#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <math.h>

#define INIT_SIZE 100
#define MAXSIZE 100

/* A calculator that takes a post fix expression and evaluates it */
int main(int argc, char *argv[]) {
	/* If no argument is given, then expression input is from stdin, otherwise from arguments */
	char **tokenArray = argv;
	//char *fromInp[];
	bool fromArgs = true;

	if (argc == 1) {
		fromArgs = false;
		//tokenArray = fromInp;
		fprintf(stderr, "Standard input not yet supported, use arguments.");
		return 1;
	}

	double valStack[MAXSIZE], v1, v2; 
	int sp = 0;

	while (--argc > 0) {
		char *token = *++argv;
		if (strlen(token) == 1 && ispunct(*token)) {
			switch (*token) {
				case '+':
					v1 = valStack[--sp];
					v2 = valStack[--sp];
					valStack[sp++] = v1 + v2;
				break;

				case '-':
					v1 = valStack[--sp];
					v2 = valStack[--sp];
					valStack[sp++] = v2 - v1;
				break;

				case '*':
					v1 = valStack[--sp];
					v2 = valStack[--sp];
					printf("%f * %f = %f", v1, v2, v1*v2);
					valStack[sp++] = v1 * v2;
				break;

				case '/':
					v1 = valStack[--sp];
					v2 = valStack[--sp];
					valStack[sp++] = v2 / v1;
				break;

				case '^':
					v1 = valStack[--sp];
					v2 = valStack[--sp];
					valStack[sp++] = pow(v1, v2);

				default:
					fprintf(stderr, "Unknown token %c", *token);
				break;
			}
		} else {
			valStack[sp++] = atof(token);
		}
	}

	printf("%.2f\n", valStack[--sp]);

	return 0;
}
