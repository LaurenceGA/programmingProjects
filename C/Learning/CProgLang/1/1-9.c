#include <stdio.h>

#define OUT 0
#define IN 1

int main() {
	int    blank  =     OUT;
	char   c;

	while((c = getchar())    != EOF) {
		if (c == ' ') {     
			if (!blank)    {
				blank = IN;
				putchar(c);
			}
		} else {
			blank = OUT;
			putchar(c);
		}
	}

	return 0;
}
