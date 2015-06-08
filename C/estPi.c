#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdlib.h>
/*
import random
import math
import time


def estimatePi(n):
    k = 0
    for n in range(n):
        xr = random.random() * 2
        yr = random.random() * 2
        d = math.sqrt((xr - 1.0)*(xr - 1.0) + (yr-1.0)*(yr-1.0))
        if d < 1:
            k += 1
    print("Finished in %f seconds" % (time.clock()))

    return (4 * k / n)*/

float random_number(float low, float hight);

long double estimatePi(int n)
{
	unsigned long k = 0;
	
	unsigned int i = 0;
	for(i = 0; i < n; i++) {
		float xr = random_number(0, 2);
		float yr = random_number(0, 2);
		double d = sqrt((xr - 1)*(xr - 1) + (yr - 1)*(yr - 1));
		if(d < 1) {
			k++;
		}
	}
	
	return (4 * (long double)k / (long double)n);
}

int main(int argc, char *argv[])
{
	// Seed the random number generator
	srand((unsigned int)time(NULL));
	
	int iterations = 100;
	//2000000000
	
	if(argc < 2) {
		printf("USAGE: estpi [precision]");
	}
	
	iterations = atoi(argv[1]);
	
	clock_t start, end;
	double cpu_time_used;
     
	start = clock();
	
	long double pi = estimatePi(iterations);
	//long double pi = estimatePi(10000000);
	printf("pi ~ %.10Lf\n\n", pi);
	
	end = clock();
	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	
	printf("Total time taken: %fseconds\n", cpu_time_used);
	
	return 0;
}

float random_number(float low, float high)
{
	// Random number between 0 and 1
	float randNum = ((float)rand()/(float)(RAND_MAX));
	return low + (randNum * high);
}
