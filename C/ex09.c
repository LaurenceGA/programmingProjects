#include <stdio.h>

int main(int argc, char *argv[])
{
	int numbers[4] = {0};
	char name[4] = {'a'};
	
	// first, print them out raw
	printf("numbers: %d %d %d %d\n",
		numbers[0], numbers[1],
		numbers[2], numbers[3]);
		
	printf("name: %c %c %c %c\n",
		name[0], name[1],
		name[2], name[3]);
		
	printf("name: %s\n", name);
	
	// Set up the numbers
	numbers[0] = 1;
	numbers[1] = 2;
	numbers[2] = 3;
	numbers[3] = 4;
	
	// set up the name
	name[0] = 'L';
	name[1] = 'G';
	name[2] = 'A';
	name[3] = '\0';
	
	// print out initialized
	printf("numbers: %d %d %d %d\n",
		numbers[0], numbers[1],
		numbers[2], numbers[3]);
		
	printf("name: %c %c %c %c\n",
		name[0], name[1],
		name[2], name[3]);
		
	printf("name: %s\n", name);
	
	// another way to use name
	char *another = "LGA";
	
	printf("another: %s\n", another);
	
	printf("another each: %c %c %c %c\n",
			another[0], another[1],
			another[2], another[3]);
	
	return 0;
}
