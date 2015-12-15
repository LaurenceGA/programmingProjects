#include <stdio.h>

/* Counts the number of space, tabs and newlines*/
int main() {
	char c;

	int newcount, spacecount, tabcount;
	newcount = spacecount = tabcount = 0;

	while((c = getchar()) != EOF) {
		switch(c) {
			case ' ':
				++spacecount;
				break;
			case '\t':
				++tabcount;
				break;
			case '\n':
				++newcount;
				break;
		}
	}

	printf("Newlines: %d\nTabs: %d\nSpaces: %d\nTotal whitespace: %d\n", 
			newcount, tabcount, spacecount, newcount + tabcount + spacecount);

	return 0;
}

