#include <stdio.h>

/* Prints a histogram of word lengths */

#define MAXWORDLEN 10

#define IN 1
#define OUT 0

int main() {
	int wordlen[MAXWORDLEN + 1] = {0};	// The extra space for words > max
	int inword = OUT;
	char c;
	int curlen = 0;

	while ((c = getchar()) != EOF) {
		if (c == ' ' || c == '\t' || c == '\n') {
			if (inword == IN) {
				inword = OUT;
				
				if (curlen > MAXWORDLEN) {
					++wordlen[MAXWORDLEN];
				} else {
					++wordlen[curlen-1];
				}
			}
		} else {
			if (inword == IN) {
				++curlen;
			} else {
				inword = IN;
				curlen = 1;
			}
		}
	}

	for (int i=0; i < MAXWORDLEN+1; ++i) {
		if (i == MAXWORDLEN) {
			printf(">%d|", i);
		} else {
			printf("%d|", i+1);
		}
		
		for (int j=0; j < wordlen[i]; ++j) {
			putchar('*');
		}

		putchar('\n');
	}

	return 0;
}
