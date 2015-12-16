#include <stdio.h>

int main(int argc, char *argv[])
{
	int i = 0;
	
	// go through each string in argv
	// argv 0 is the name of the script
	for(i = 1; i < argc; i++) {
		printf("arg %d: %s\n", i, argv[i]);
	}
	
	// make array of strings
	char *countries[] = {
		"New Zealand", "Australia", "Germany", "United States of America"
	};
	int num_country = 4;
	
	for(i = 0; i < num_country; i++) {
		printf("state: %d: %s\n", i, countries[i]);
	}
	
	return 0;
}
