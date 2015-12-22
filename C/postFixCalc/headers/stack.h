#ifndef STACK_H
#define STACK_H

/* Defines a stack implemented as a linked list.
 * It holds double values. 
 * It has the interface:
 * newStack()	-	 Initialise
 * pop()	-	Pop a value off the stack
 * push()	-	Push a value onto the stack
 * freeStack()	-	Free memory
 * */

// Make it an easily accesible type
typedef struct NumStack NumStack;
typedef struct NumNode NumNode;

// The main list struct
struct NumStack {
	NumNode *head;
	int length;
};

// The Node struct used in the list
struct NumNode {
	double val;
	NumNode *next;
};

NumNode *newNode(double x);

NumStack *newStack();
void push(NumStack *list, double x);
double pop(NumStack *list);
int isEmpty(NumStack *list);
void freeStack(NumStack *list);

#endif
