// Implementation of a stack as a linked list
#include <stdio.h>
#include <stdlib.h>

#include "headers/stack.h"

NumNode *newNode(double x) {
	NumNode *node = (NumNode *) malloc(sizeof(NumNode));
	
	node->val = x;
	node->next = NULL;
	
	return node;
}

NumStack *newStack() {
	NumStack *newStk = (NumStack *) malloc(sizeof(NumStack));
	newStk->head = NULL;
	newStk->length = 0;

	return newStk;
}

void push(NumStack *list, double x) {
	if (isEmpty(list)) {
		list->head = newNode(x);
	} else {
		NumNode *oldHead = list->head;
		list->head = newNode(x);
		list->head->next = oldHead;
	}

	list->length += 1;	
}

double pop(NumStack *list) {
	if (isEmpty(list)) {
		fprintf(stderr, "%s\n", "Stack empty!");
		return 0;
	}

	NumNode *top = list->head;
	double val = top->val;
	list->head = list->head->next;

	free(top);

	list->length -= 1;
	return val;
}

int isEmpty(NumStack *list) {
	return list->head == NULL;
}

void freeStack(NumStack *list) {
	if (!isEmpty(list)) {
		NumNode *next;

		for ( ; list->head != NULL; list->head = next) {
			next = list->head->next;
			free(list->head);
		}	
	}
	free(list);
}
