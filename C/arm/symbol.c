#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#include "headers/symbol.h"

static Symbol *symlist = NULL;

Symbol *install(char *s, int typ, double val, bool cnst) {
	Symbol *sp = (Symbol *) malloc(sizeof(Symbol));
	if (sp == NULL) {
		fprintf(stderr, "Failed to allocate memory for new symbol\n");
		abort();
	}

	sp->name = (char *) malloc(strlen(s) + 1);
	if (sp->name == NULL) {
		fprintf(stderr, "Failed to allocate memory for new symbol name\n");
		abort();
	}

	strcpy(sp->name, s);
	sp->type = typ;
	sp->val = val;
	sp->cnst = cnst;
	sp->next = symlist;
	symlist = sp;
	return sp;
}

Symbol *lookup(char *s) {
	for (Symbol *sp = symlist; sp != NULL; sp=sp->next) {
		if (strcmp(sp->name, s) == 0) {
			return sp;
		}
	}

	return NULL;
}
