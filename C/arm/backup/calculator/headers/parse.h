#ifndef PARSE_H
#define PARSE_H

#include <stdio.h>
#include <stdbool.h>

#include "lexer.h"
#include "ast.h"

/*
Prases the grammar:

StatementList:
	((Statement)?\n)* END

Statement:	
	Expression

Expression:
	Term(('+'|'-')Term)*

Term:
	Factor(('*'|'/'|'%')Factor)*

Factor:
	['-'|'+']Expo

Expo:
	Final('^'Final)*

Final:
	NUM|'('Expression')'

This produces the following operator precedence
Operator	Description				Associativity
^			Exponentiate			Right
+-			Unary plus/minus		N/A
*%/			Multiplicative & Mod	Left
+-			Additive				Left

*/

bool parse(FILE *f);

bool StatementList(Lexer *l, Lexval *val);

astNode *Statement(Lexer *l, Lexval *val);
astNode *Expression(Lexer *l, Lexval *val);
astNode *Term(Lexer *l, Lexval *val);
astNode *Factor(Lexer *l, Lexval *val);
astNode *Expo(Lexer *l, Lexval *val);
astNode *Final(Lexer *l, Lexval *val);

void syntaxError(char *wanted, char *got);

#endif
