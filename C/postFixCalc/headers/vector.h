#ifndef VECTOR_H
#define VECTOR_H

#define INIT_SIZE 20
#define GROW_FACTOR 2

/* Defines a very simple growable array */
typedef struct Vector Vector;

struct Vector {
	void **data;
	int size;
	int capacity;
};

Vector *newVector();
void append(Vector *v, void *item);
void freeVector(Vector *v);

#endif
