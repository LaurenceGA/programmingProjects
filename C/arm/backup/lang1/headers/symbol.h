#ifndef SYMBOL_H
#define SYMBOL_H

#include <stdbool.h>

typedef struct Symbol {
	char *name;
	short type;				// VAR, UNDEF, BLTIN etc.
	short varType;			// Only used if type is VAR
	bool cnst;
	union {
		double val;			// VAR
		double (*ptr)();	// BLTIN
		char *str;			// STRING
	};
	struct Symbol *next;
} Symbol;

Symbol *install(char *s, int typ, double val, bool cnst);
Symbol *lookup(char *s);

#endif
