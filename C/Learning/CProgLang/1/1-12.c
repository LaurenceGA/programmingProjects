#include <stdio.h>

/* Counts the number of space, tabs and newlines*/
int main() {
	char c, prev;
	prev = EOF;

	while((c = getchar()) != EOF) {
		if(c == ' ') {
			if (prev != c) {
				putchar('\n');
			}
		} else if(c != '\t') {
			if(c == '\n') {
				if (prev != c) {
					putchar(c);
				}
			} else {
				putchar(c);
			}
		}

		prev = c;
	}

	return 0;
}

