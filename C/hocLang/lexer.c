#include "headers/lexer.h"

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

Lexer *newLexer(FILE *f) {
	Lexer *newLex = (Lexer *) malloc(sizeof(Lexer));
	if (!newLex) {
		fprintf(stderr, "%s\n", "Memory allocation failed for lexer");
	}
	newLex->inpFile = f;
	newLex->lineCount = 1;
	//newLex->currentChar = fgetc(newLex->inpFile);

	return newLex;
}

void freeLexer(Lexer *l) {
	free(l);
}

Token getNextToken(Lexer *l) {
	int c;

	skipWhiteSpace(l);

	if ((c = fgetc(l->inpFile)) == EOF) {
		Token t = {END, 0};
		return t;
	} else if (c == '\n') {
		l->lineCount++;
	} else if (c == '.' || isdigit(c)) {
		ungetc(c, l->inpFile);
		return getNum(l);
	}
	Token t = {NUMBER, "5"};
	return t;
}

Token getNum(Lexer *l) {
	char buff[NUMLEN];
	int c, i = 0;

	while ((c = fgetc(l->inpFile)) == '.' || isdigit(c)) {
		buff[i++] = c;
	}
	buff[i] = '\0';
	ungetc(c, l->inpFile);
	return buff;
}

void skipWhiteSpace(Lexer *l) {
	int c;

	while ((c = fgetc(l->inpFile)) == ' ' || c == '\t')
		;
	ungetc(c, l->inpFile);
}

void syntaxError(char c, int line) {
	fprintf(stderr, "Syntax error at char %c, on line %d\n", c, line);
}
