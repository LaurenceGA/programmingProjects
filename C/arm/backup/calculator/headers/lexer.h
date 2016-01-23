#ifndef LEXER_H
#define LEXER_H

#include <stdio.h>
#include <stdbool.h>

/* Lexer tokenizes an input stream, passed as an open file 
 * Does not handle the openeing or closing of files */

// All the tokens types that can be parsed
typedef enum Token_t Token_t;
enum Token_t {
	UNKNOWN,
	END,
	NL,			// \n
	NUMBER,		// 1.2, .5, 3
	PLUS,		// +
	MINUS,		// -
	MUL,		// *
	DIV,		// /
	MOD,		// %
	EXP,		// ^
	LPAREN,		// (
	RPAREN		// )
};

// For error message purposes
extern char *tokens[];

// Stores the value information about the token to go with the type
typedef union Lexval Lexval;
union Lexval {
	double value;
};

// Holds info about the lexer for a given stream
typedef struct Lexer Lexer;
struct Lexer {
	FILE *inpFile;
	char currentChar;

	bool buffFull;
	Token_t buffer;
	Lexval buffVal;
};

// Public
Lexer *newLexer(FILE *f);	// Allocate memory and initialize
void freeLexer(Lexer *l);	// Free memory
Token_t getNextToken(Lexer *l, Lexval *val);	// Returns what type and sets value if appropriate;
void unGetToken(Lexer *l, Lexval *val, Token_t tok);

// Private
void advance(Lexer *l);		// Move the lexer forward a character
void skipWhitespace(Lexer *l);	// Spaces and tabs are skipped


#endif
