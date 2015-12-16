#include "headers/vector.h"
#include <stdlib.h>
#include <stdio.h>

void vector_init(Vector *v) {
	// Init size and capacity
	v->size = 0;
	v->capacity = INIT_SIZE;

	// Allocate memory
	v->data = (char *) malloc(v->capacity * sizeof(char *));
}

void vector_append(Vector *v, char *s) {
	// Make sure the vector has room
	vector_expand(v);

	v->data[v->size++] = s;
}

char *vector_get(Vector *v, int ind) {
	if (ind >= v->size || ind < 0) {
		fprintf(stderr, "Array index out of bounds.");
		exit(1);
	} else {
		return v->data[ind];
	}
}

void vector_set(Vector *v, int ind, char *s) {
	// Expand to index, "" in between
	while (ind >= v->size)
		vector_append(v, "");

	v->data[ind] = value;
}

void vector_expand(Vector *v) {
	if (v->size >= v->capacity) {
		v->capacity *= 2;
		v->data = realloc(v->data, v->capacity * sizeof(char *));
	}
}

void vector_free(Vector *v) {
	free(vector->data);
}
