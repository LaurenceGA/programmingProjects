#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>

#include "headers/lexer.h"

// For error messages
// Lines up with Token_t enum
char *tokens[] = {
	"unknown",
	"EOF",
	"new line",
    "number",
    "+",
    "-",
    "*",
    "/",
	"%",
	"^",
	"(",
	")",
	"identifier"
};


Lexer *newLexer(FILE *f) {
	// Multiple lexers can be going at once
	Lexer *newLex = (Lexer *) malloc(sizeof(Lexer));
	if (newLex == NULL) {
		fprintf(stderr, "%s\n", "Could not allocate new lexer");
		abort();
	}

	newLex->inpFile = f;
	newLex->buffFull = false;

	return newLex;
}

void freeLexer(Lexer *l) {
	free(l);
}

void advance(Lexer *l) {
	l->currentChar = fgetc(l->inpFile);
}

Token_t getNextToken(Lexer *l, Lexval *val) {
	// BUFFERED TOKEN
	if (l->buffFull) {
		*val = l->buffVal;	// Copy stored value to provided address

		l->buffFull = false;
		return l->buffer;
	}

	// NORMAL LEXING
	skipWhitespace(l);	// Space and tab
	
	advance(l);
	
	// NUMBER (unary minus is handled in parsing stage)
	if (l->currentChar == '.' || isdigit(l->currentChar)) {
		ungetc(l->currentChar, l->inpFile);
		fscanf(l->inpFile, "%lf", &val->value);
		return NUMBER;
	}

	switch (l->currentChar) {
		case '\n':
			return NL;
			break;

		case EOF:
			return END;
			break;

		case '+':
			return PLUS;
			break;

		case '-':
			return MINUS;
			break;

		case '*':
			return MUL;
			break;

		case '/':
			// Comments
			advance(l);
			if (l->currentChar == '/') {
				while (l->currentChar != '\n')	// Throw away comment until we find the end of the line
					advance(l);
				return NL;
			} else {		// Otherwise it's divide
				ungetc(l->currentChar, l->inpFile);
				return DIV;
			}
			break;

		case '%':
			return MOD;
			break;

		case '^':
			return EXP;
			break;

		case '(':
			return LPAREN;
			break;

		case ')':
			return RPAREN;
			break;

		default:
			return UNKNOWN;
			break;
	}

	return UNKNOWN;
}

void unGetToken(Lexer *l, Lexval *val, Token_t tok) {
	// Token buffering to allow for lookahead
	if (l->buffFull) {
		// Error, don't unget twice
		fprintf(stderr, "Buff already full\n");
		abort();
	} else {
		l->buffFull = true;
		l->buffer = tok;
		l->buffVal = *val;
	}
}

void skipWhitespace(Lexer *l) {
	advance(l);
	while (l->currentChar == ' ' || l->currentChar == '\t')
		advance(l);
	ungetc(l->currentChar, l->inpFile);	// Went too far, don't need that
}

