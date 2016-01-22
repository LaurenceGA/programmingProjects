#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

#include "headers/ast.h"
#include "headers/lexer.h"
#include "headers/symbol.h"

extern bool SHOWTREE;

static bool brk = false;
static bool cont = false;

double getValue(astNode *root) {
	switch (root->type) {
		case NUM_nd:
			return root->value;
			break;
		
		case ADD_nd:
			return getValue(root->op.left) + getValue(root->op.right);
			break;

		case SUB_nd:
			return getValue(root->op.left) - getValue(root->op.right);
			break;

		case MUL_nd:
			return getValue(root->op.left) * getValue(root->op.right);
			break;

		case DIV_nd:
			{
				double rval = getValue(root->op.right);
				if (rval == 0) {
					fprintf(stderr, "Divison by 0.\n");
					abort();
				}
				return getValue(root->op.left) / rval;
			}
			break;

		case EXP_nd:
			return pow(getValue(root->op.left), getValue(root->op.right));
			break;
		
		case MOD_nd:
			return (int) getValue(root->op.left) % (int) getValue(root->op.right);
			break;

		case NEG_nd:
			return -getValue(root->next);
			break;

		case NOT_nd:
			return !getValue(root->next);

		case GT_nd:
			return (double) getValue(root->op.left) > getValue(root->op.right);
		
		case LT_nd:
			return (double) getValue(root->op.left) < getValue(root->op.right);

		case GE_nd:
			return (double) getValue(root->op.left) >= getValue(root->op.right);

		case LE_nd:
			return (double) getValue(root->op.left) <= getValue(root->op.right);

		case EQ_nd:
			return (double) getValue(root->op.left) == getValue(root->op.right);

		case NEQ_nd:
			return (double) getValue(root->op.left) != getValue(root->op.right);

		case AND_nd:
			if (!getValue(root->op.left))
				return 0;
			if (!getValue(root->op.right))
				return 0;
			return 1;

		case OR_nd:
			if (getValue(root->op.left))
				return 1;
			if (getValue(root->op.right))
				return 1;
			return 0;

		case VAR_nd:
			if (root->sym->type == UNDEF) {
				fprintf(stderr, "Variable '%s' is undefined.\n", root->sym->name);
				abort();
			}
			return root->sym->val;
		
		case BLTIN_nd:
			return root->sym->ptr(getValue(root->next));

		default:
			fprintf(stderr, "Unable to get ast node value\n");
			abort();
	}
	return 0;
}

astNode *newNode(nodeType typ) {
	astNode *node = (astNode *) malloc(sizeof(astNode));
	if (node == NULL) {
		fprintf(stderr, "Failed to allocate memory creating astNode\n");
		abort();
	}

	node->type = typ;
	node->value = 0;
	node->str = NULL;
	node->op.left = node->op.right = node->next = NULL;

	return node;
}

astNode *opNode(nodeType typ, astNode *left, astNode *right) {
	astNode *opNd = newNode(typ);

	opNd->op.left = left;
	opNd->op.right = right;

	return opNd;
}

astNode *unopNode(nodeType typ, astNode *next) {
	astNode *unopNd = newNode(typ);

	unopNd->next = next;

	return unopNd;
}

astNode *numNode(double value) {
	astNode *numNd = newNode(NUM_nd);

	numNd->value = value;

	return numNd;
}

astNode *varNode(Lexval *lval) {
	astNode *varNd = newNode(VAR_nd);

	varNd->sym = lval->sym;

	return varNd;
}

astNode *strNode(Lexval *lval) {
	astNode *strNd = newNode(STR_nd);

	strNd->str = (char *) malloc(strlen(lval->str) + 1);
	strcpy(strNd->str, lval->str);

	return strNd;
}

void execute(astNode *root) {
	if (SHOWTREE) {		// Set by cmd line option
		printTree(root, 0, false);
	}
	
	if (root->type == ASGN_nd) {
		// The symbol we're assigning to
		Symbol *s = root->op.left->sym;
		if (s->cnst) {
			fprintf(stderr, "Cannot assign to constant value '%s'\n", s->name);
			abort();
		}

		if (root->op.right->type == STR_nd) {
			if (s->type == STRING)
				free(s->str);
			s->type = STRING;
			s->str = (char *) malloc(strlen(root->op.right->str)+1);
			strcpy(s->str, root->op.right->str);
		} else {
			s->type = VAR;
			s->val = getValue(root->op.right);
		}
	} else if (root->type == IF_nd) {
		if (getValue(root->next) != 0) {
			execute(root->op.left);
		} else if (root->op.right != NULL) {
			execute(root->op.right);
		}
	} else if (root->type == WHILE_nd) {
		while (getValue(root->op.left) != 0) {
			execute(root->op.right);
			if (cont) {
				cont = false;
				continue;
			}
			if (brk) {
				brk = false;
				break;
			}
		}
	} else if (root->type == STATEMENT_nd) {
		if (root->op.left != NULL) {
			execute(root->op.left);
		}
		if (!cont && !brk) {
			if (root->next != NULL) {
				execute(root->next);
			}
		}
	} else if (root->type == BREAK_nd) {
		brk = true;
	} else if (root->type == CONTINUE_nd) {
		cont = true;
	} else if (root->type == PRINT_nd) {
		if (root->next != NULL) {
			for (astNode *p = root->next; p != NULL; p = p->next) {
				if (p->op.left != NULL) {
					if (p->op.left->type == STR_nd)
						printf("%s", p->op.left->str);
					else
						printf("%g", getValue(p->op.left));
				} else {
					fprintf(stderr, "Empty argument node\n");
					abort();
				}
			}
		} else printf("\n");
	} else if (root->type != STR_nd) {
		getValue(root);
	}
}

void printTree(astNode *root, int level, bool nxt) {
	if (root != NULL) {
		// LEFT
		if (root->op.left != NULL) {
			printTree(root->op.left, level + 1, false);
		}
		
		// ROOT
		if (nxt) {
			printf("───┼");
		} else {
			for (int i=0; i < level; i++) {
				if (i == level-1)
					printf("───┼");
				else
					printf("   ├");
			}
		}

		switch (root->type) {
			case NUM_nd:
				printf("%g\n", root->value);
				break;
			case ADD_nd:
				printf("ADD\n");
				break;
			case SUB_nd:
				printf("SUB\n");
				break;
			case MUL_nd:
				printf("MUL\n");
				break;
			case DIV_nd:
				printf("DIV\n");
				break;
			case EXP_nd:
				printf("EXPO\n");
				break;
			case MOD_nd:
				printf("MOD\n");
				break;
			case NEG_nd:
				printf("NEG");
				break;
			case ASGN_nd:
				printf("ASGN\n");
				break;
			case VAR_nd:
				printf("%s\n", root->sym->name);
				break;
			case BLTIN_nd:
				printf("%s", root->sym->name);
				break;
			case NOT_nd:
				printf("NOT");
				break;
			case GT_nd:
				printf("GT\n");
				break;
			case LT_nd:
				printf("LT\n");
				break;
			case GE_nd:
				printf("GE\n");
				break;
			case LE_nd:
				printf("LE\n");
				break;
			case EQ_nd:
				printf("EQ\n");
				break;
			case NEQ_nd:
				printf("NEQ\n");
				break;
			case AND_nd:
				printf("AND\n");
				break;
			case OR_nd:
				printf("OR\n");
				break;
			case IF_nd:
				printf("IF");
				break;
			case WHILE_nd:
				printf("WHILE");
				break;
			case STATEMENT_nd:
				printf("STMNT");
				break;
			case BREAK_nd:
				printf("BREAK");
				break;
			case CONTINUE_nd:
				printf("CONTINUE");
				break;
			case PRINT_nd:
				printf("PRINT");
				break;
			case ARG_nd:
				printf("ARG");
				break;
			default:
				printf("Unknown");
				break;
		}
	}

	// Next
	if (root->next != NULL) {
		printTree(root->next, level, true);
	}

	// RIGHT
	if (root->op.right != NULL) {
		printTree(root->op.right, level + 1, false);
	}
}

void freeTree(astNode *root) {
	if (root != NULL) {
		if (root->next != NULL) freeTree(root->next);
		if (root->op.left != NULL) freeTree(root->op.left);
		if (root->op.right != NULL) freeTree(root->op.right);
		if (root->str != NULL) free(root->str);
		free(root);
	}
}
