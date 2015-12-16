#include <stdio.h>

/* Should remove all comments from any C program */

/* This includes open comments */
// And line ending comments
// Quotes should be handled correctly

#define INLINE 2
#define IN 1
#define OUT 0

char test[] = "This is a test string // that has /**/ comments stuff in it";
char testchar = '\\';

int main() {
	char c;
	int inquotes = OUT;
	int inComment = OUT;

	while ((c = getchar()) != EOF) {
		if (c == '/' && inComment == OUT && inquotes == OUT) {
			c = getchar();
			if (c == '/') {
				inComment = INLINE;
			} else if (c == '*') {
				inComment = IN;
			}
		} else if (c == '\'' || c == '\"') {
			if (inquotes == IN)
				inquotes = OUT;
			else
				inquotes = IN;
		} else if (c == '\n') {
			if (inComment == INLINE) {
				inComment = OUT;
			}
		} else if (c == '*') {
			if (inComment == IN) {
				c = getchar();
				if (c == '/') {
					inComment = OUT;
					continue;
				}
			}
		}
		
		if (inComment == OUT) {
			putchar(c);
		}
	}

	return 0;
}
