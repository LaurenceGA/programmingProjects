#include <stdio.h>

int main() {
	char   c;

	while((c = getchar())    != EOF) {
		switch(c) {
			case '\t':
				printf("\\t");
				break;
			case '\\':
				printf("\\\\");
				break;
			case '\b':
				printf("\\b");
				break;
			default:
				putchar(c);
		}
	}

	return 0;
}
