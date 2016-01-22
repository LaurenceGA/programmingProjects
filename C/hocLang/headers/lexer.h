#ifndef LEXER_H
#define LEXER_H

#include <stdio.h>

#define NUMLEN 32

// Terminals
enum TOKEN_TYPE {
	END,
	NUMBER,
	OPERATOR
};

typedef struct Token Token;
typedef enum TOKEN_TYPE Token_t;

// E.G (NUMBER, '5.3')
// (OPERATOR, '+')
struct Token {
	Token_t type;
	char *value;
};

typedef struct Lexer Lexer;

struct Lexer {
	FILE *inpFile;
	int lineCount;
	int currentChar;
};

Lexer *newLexer(FILE *f);	// Allocate memory for the lexer
void freeLexer(Lexer *l);	// Free memory for the lexer


Token getNextToken(Lexer *l);		// Get the next token
Token getNum(Lexer *l);			// Parse a double
void skipWhiteSpace(Lexer *l);		// \t, ' '
void syntaxError(char c, int line);		// Which char and which line

#endif
