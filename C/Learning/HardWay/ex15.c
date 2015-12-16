#include <stdio.h>

int main(int argc, char *argv[])
{
	// create two arrays we care about
	int ages[] = {23, 43, 12, 89, 2};
	char *names[] = {
		"Alan", "Frank",
		"Mary", "John", "Lisa"
	};
	
	 // safely get the size of ages
	int count = sizeof(ages) / sizeof(int);
	int i = 0;

	// first way using indexing
	for(i = 0; i < count; i++) {
		printf("%s has %d years alive.\n",
				names[i], ages[i]);
	}

	printf("---\n");
    
	// set up pointers to start of the arrays
	int *cur_age = ages;
	char **cur_name = names;
	
	printf("Address of *cur_age is %p\n", cur_age);
	printf("Address of *cur_name is %p\n", cur_name);

	// second way using pointers
	for(i = 0; i < count; i++) {
		printf("%s is %d years old.\n",
				*(cur_name+i), *(cur_age+i));
	}
	
	printf("---\n");
	
	// third way, the pointers are arrays
	for(i = 0; i < count; i++) {
		printf("%s is %d years old again.\n",
				cur_name[i], cur_age[i]);
	}
	
	printf("---\n");
	
	// fourth way with pointers and a stupid complex way
	for(cur_name = names, cur_age = ages;
		(cur_age - ages) < count;
		cur_name++, cur_age++)
	{
		printf("%s has lived %d years so far.\n",
				*cur_name, *cur_age);
	}

	return 0;
}
