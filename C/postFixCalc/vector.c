#include <stdio.h>
#include <stdlib.h>

#include "headers/vector.h"

Vector *newVector() {
	Vector *newVect = (Vector *) malloc(sizeof(Vector));
	if (!newVect) {
		// Error
	}

	newVect->capacity = INIT_SIZE;
	newVect->size = 0;
	newVect->data = malloc(sizeof(void *) * newVect->capacity);
	if (!newVect->data) {
		// Error
	}

	return newVect;
}

void append(Vector *v, void *item) {
	if (v->size == v->capacity) {
		v->capacity *= GROW_FACTOR;
		v->data = realloc(v->data, sizeof(void *) * v->capacity);
		if (!v->data) {
			// Error
		}
	}

	v->data[v->size++] = item;
}

void freeVector(Vector *v) {
	free(v->data);
	free(v);
}
