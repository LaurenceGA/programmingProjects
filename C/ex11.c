#include <stdio.h>

int main(int argc, char *argv[])
{
    // go through each string in argv

    int i = 0;
    while(i < argc) {
        printf("arg %d: %s\n", i, argv[i]);
        i++;
    }

    // let's make our own array of strings
    char *countries[] = {
		"New Zealand", "Australia", "Germany", "United States of America"
	};

    int num_country = 4;
    i = 0;  // watch for this
    while(i < num_country) {
        printf("countries %d: %s\n", i, countries[i]);
        i++;
    }

    return 0;
}
