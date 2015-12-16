#include <stdio.h>

#define MAXLINE 1000

void reverse(char s[]) {
	int j;
	for(j=0; s[j] != '\0'; ++j) { }
	--j;

	for (int i=0; i < j; ++i) {
		char ch = s[j];
		s[j] = s[i];
		s[i] = ch;
		--j;
	}
}

int getline(char s[], int lim) {
	int c, i;

	for (i=0; i<lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
		s[i] = c;
	if (c == '\n') {
		s[i] = c;
		++i;
	}
	s[i] = '\0';
	return i;
}

int main() {
	char line[MAXLINE];
	int len = 0;

	while ((len = getline(line, MAXLINE)) > 0) {
		reverse(line);
		printf(line);
	}

	return 0;
}
