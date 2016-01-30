#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#include "headers/ast.h"

extern bool SHOWTREE;

double getValue(astNode *root) {
	switch (root->type) {
		case NUM:
			return root->value;
			break;
		
		case ADD:
			return getValue(root->op.left) + getValue(root->op.right);
			break;

		case SUB:
			return getValue(root->op.left) - getValue(root->op.right);
			break;

		case MULTIPLY:
			return getValue(root->op.left) * getValue(root->op.right);
			break;

		case DIVIDE:
			return getValue(root->op.left) / getValue(root->op.right);
			break;

		case EXPO:
			return pow(getValue(root->op.left), getValue(root->op.right));
			break;
		
		case MODULO:
			return (int) getValue(root->op.left) % (int) getValue(root->op.right);
			break;

		case NEG:
			return -getValue(root->next);

		default:
			fprintf(stderr, "Unknow ast node\n");
			abort();
	}
	return 0;
}

astNode *opNode(nodeType typ, astNode *left, astNode *right) {
	astNode *newNode = (astNode *) malloc(sizeof(astNode));
	if (newNode == NULL) {
		fprintf(stderr, "Failed to allocate memory of op node\n");
		abort();
	}

	newNode->type = typ;
	newNode->op.left = left;
	newNode->op.right = right;
	newNode->next = NULL;	// In case it's accessed

	return newNode;
}

astNode *unopNode(nodeType typ, astNode *next) {
	astNode *newNode = (astNode *) malloc(sizeof(astNode));
	if (newNode == NULL) {
		fprintf(stderr, "Failed to allocate memory of unop node\n");
		abort();
	}

	newNode->type = typ;
	newNode->next = next;
	// In case they're accessed
	newNode->op.left = NULL;
	newNode->op.right = NULL;

	return newNode;
}

astNode *numNode(double value) {
	astNode *newNode = (astNode *) malloc(sizeof(astNode));
	if (newNode == NULL) {
		fprintf(stderr, "Failed to allocate memory of num node\n");
		abort();
	}
	newNode->type = NUM;
	newNode->value = value;
	// In case they're accessed
	newNode->op.left = NULL;
	newNode->op.right = NULL;
	newNode->next = NULL;

	return newNode;
}

void execute(astNode *root) {
	if (SHOWTREE) {		// Set by cmd line option
		printTree(root, 0);
	}

	printf("%g\n", getValue(root));
}

void printTree(astNode *root, int level) {
	if (root != NULL) {
		// LEFT
		if (root->op.left != NULL) {
			printTree(root->op.left, level + 1);
		}
		
		// ROOT
		for (int i=0; i < level; i++) {
			if (i == level-1)
				printf("───┼");
			else
				printf("   ├");
		}

		switch (root->type) {
			case NUM:
				printf("%g\n", root->value);
				break;
			case ADD:
				printf("ADD\n");
				break;
			case SUB:
				printf("SUB\n");
				break;
			case MULTIPLY:
				printf("MUL\n");
				break;
			case DIVIDE:
				printf("DIV\n");
				break;
			case EXPO:
				printf("EXPO\n");
				break;
			case MODULO:
				printf("MOD\n");
				break;
			case NEG:
				printf("-");
				break;
			default:
				printf("Unknown");
				break;
		}
	}

	// Next
	if (root->next != NULL) {
		printTree(root->next, 0);
	}

	// RIGHT
	if (root->op.right != NULL) {
		printTree(root->op.right, level + 1);
	}
}

void freeTree(astNode *root) {
	if (root != NULL) {
		freeTree(root->op.left);
		freeTree(root->op.right);
		free(root);
	}
}
