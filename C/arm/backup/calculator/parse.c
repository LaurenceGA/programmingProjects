#include <string.h>
#include <stdlib.h>

#include "headers/parse.h"
#include "headers/lexer.h"
#include "headers/ast.h"

bool parse(FILE *f) {
	Lexer *lex = newLexer(f);
	Lexval val;		// Stores extra info about token

	bool parsed = StatementList(lex, &val);

	freeLexer(lex);

	return parsed;
}

bool StatementList(Lexer *l, Lexval *val) {
	// ((Statement)?\n)* END
	//printf(">");	// prompt
	Token_t tok;
	while ((tok = getNextToken(l, val)) != END) {	// Until EOF
		if (tok != NL) {				// Allows line to be emptry
			unGetToken(l, val, tok);	// Need token we requested in other functions

			astNode *statement = Statement(l, val);
			if ((tok = getNextToken(l, val)) != NL) {	// Statement ends in newline
				syntaxError("newline", tokens[tok]);
			}

			// Execute as we parse
			execute(statement);
			free(statement);
		}
		//printf(">");
	}

	return true;	// Parsed just fine
}

astNode *Statement(Lexer *l, Lexval *val) {
	// Expression
	return Expression(l, val);
}

astNode *Expression(Lexer *l, Lexval *val) {
	// Tem(('+'|'-')Term)*
	astNode *node = Term(l, val);

	Token_t tok;
	// Check if next token is a operator of +- precedence
	while ((tok = getNextToken(l, val)) == PLUS || tok == MINUS) {
		if (tok == PLUS) {
			node = opNode(ADD, node, Term(l, val));
		} else {
			node = opNode(SUB, node, Term(l, val));
		}
	}

	unGetToken(l, val, tok);	// If it wasn't, give it back

	return node;
}

astNode *Term(Lexer *l, Lexval *val) {
	// Factor(('*'|'/'|'%')Factor)*
	astNode *node = Factor(l, val);

	Token_t tok;
	// Check if of */% precedence
	while ((tok = getNextToken(l, val)) == MUL || tok == DIV || tok == MOD) {
		if (tok == MUL) {
			node = opNode(MULTIPLY, node, Factor(l, val));
		} else if (tok == DIV) {
			node = opNode(DIVIDE, node, Factor(l, val));
		} else if (tok == MOD) {
			node = opNode(MODULO, node, Factor(l, val));
		} else {
			// Impossible
		}
	}

	unGetToken(l, val, tok);	// If not, give back

	return node;
}

astNode *Factor(Lexer *l, Lexval *val) {
	// ['+'|'-']Expo
	Token_t tok;
	if ((tok = getNextToken(l, val)) == PLUS || tok == MINUS) {
		if (tok == MINUS) {
			return unopNode(NEG, Expo(l, val));
		} else {
			return Expo(l, val);
		}
	}

	unGetToken(l, val, tok);

	return Expo(l, val);
}

astNode *Expo(Lexer *l, Lexval *val) {
	// Final(^Final)*
	astNode *node = Final(l, val);

	Token_t tok;
	while ((tok = getNextToken(l, val)) == EXP) {
		// EXP is right associative
		if (node->type == NUM) {
			node = opNode(EXPO, node, Final(l, val));
		} else if (node->type == EXPO) {
			// Final right-most exp op
			astNode *rightOp = node;
			while (rightOp->op.right->type != NUM) {
				rightOp = rightOp->op.right;
			}
			rightOp->op.right = opNode(EXPO, rightOp->op.right, Final(l, val));
		} else {
			// Impossible
		}
	}

	unGetToken(l, val, tok);	// Don't need it

	return node;
}

astNode *Final(Lexer *l, Lexval *val) {
	// NUM|'('Expression')'
	Token_t tok = getNextToken(l, val);
	if (tok == NUMBER) {
		return numNode(val->value);
	} else if (tok == LPAREN) {							// Parse '('
		astNode *node = Expression(l, val);				// Prase Expression
		if ((tok = getNextToken(l, val)) != RPAREN) {	// Parse ')'
			syntaxError(")", tokens[tok]);
		}
		return node;
	}

	syntaxError("number", tokens[tok]);
	return NULL;
}

void syntaxError(char *wanted, char *got) {
	fprintf(stderr, "Syntax error: wanted '%s', got '%s'\n", wanted, got);
	abort();
}
