#ifndef AST_H
#define AST_H

typedef enum nodeType nodeType;
enum nodeType {
	NUM,
	ADD,
	SUB,
	MULTIPLY,
	DIVIDE,
	EXPO,
	MODULO,
	NEG
};

typedef struct astNode astNode;
struct astNode {
	nodeType type;
	float value;	// For number nodes
	astNode *next;
	struct {
		astNode *left;
		astNode *right;
	} op;
};

double getValue(astNode *root);		// Returns the value of a tree - called on operators

astNode *opNode(nodeType typ, astNode *left, astNode *right);	// Binary operator +-^%* etc.
astNode *unopNode(nodeType typ, astNode *next);	// Unary operators
astNode *numNode(double value);	// Just numbers

void execute(astNode *root);
void freeTree(astNode *root);

void printTree(astNode *root, int level);	// Recursive print

#endif
