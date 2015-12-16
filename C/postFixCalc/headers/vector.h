/* A resiable array. Specifically an array of strings array */
#ifndef VECTOR_H
#define VECTOR_H

#define INIT_SIZE 10

typedef struct {
	int size;
	int capacity;
	char *data[];
} Vector;

void vector_init(Vector *v);

void vector_append(Vector *v, char *s);

void vector_set(Vector *v, int ind, char *s);

char *vector_get(Vector *v, int ind);

void vector_expand(Vector *v);

void vector_free(Vector *v);

#endif
