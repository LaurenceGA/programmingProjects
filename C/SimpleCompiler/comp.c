#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdbool.h>

#define MAXLINE 1024

void runcmd(char *loc, char *args[]);
void unspecial(char *rawstring, int lim);

int main(int argc, char *argv[]) {
	bool removeTempC = true;
	char c;
	
	while(--argc > 1) {
		++argv;
		if ((*argv)++[0] == '-') {
			while ((c = (*argv)++[0]) != '\0') {
				switch (c) {
					case 'r':
						removeTempC = false;
						break;
					default:
						printf("Incorrect optional argument %c.\n", c);
						break;
				}
			}
		}
	}

	/* There must be one argument, that is a file name */
	if (argc != 1) {
		fprintf(stderr, "Incorrect number of arguments.\nusage: lcomp [-r] file.L\n");
		return 1;
	}

	/* It must have the extension '.L' */
	char *filename = argv[1];
	int i;

	for (i=0; filename[i+1] != '\0'; i++); // Go to the end of the filename

	if (!(i && filename[i] == 'L' && filename[i-1] == '.')) {
		fprintf(stderr, "Invalid .L filename.\n");
		return 1;
	}
	 /* Open the source .L file */

	FILE *sfile; 
		
	if ((sfile = fopen(filename, "r")) == NULL) {
		fprintf(stderr, "Can't open %s.\n", filename);
		return 1;
	}

	/* Create the .c file to be written to */
	FILE *ctemp;
	char *tempName = strcat(filename, "temp.c");

	if ((ctemp = fopen(tempName, "w")) == NULL) {
		fprintf(stderr, "Couldn't create temp .c file\n");
		return 1;
	}

	char data[MAXLINE];
	fread(data, sizeof(char), MAXLINE, sfile);
	unspecial(data, MAXLINE);

	for (i=0; data[i+1] != EOF; i++);	// Go to end of data
	data[i] = '\0';

	// Write to .c file
	fprintf(ctemp, "#include <stdio.h>\n"
					"int main(int argc, char *argv[]) {\n");

	fprintf(ctemp, "printf(\"%s\");", data);
	
	fprintf(ctemp, "\nreturn 0;}");

	fclose(ctemp);
	fclose(sfile);
	
	char *args[] = {"/usr/bin/gcc", tempName, "-std=c11", "-o", "hello", NULL};
	runcmd("/usr/bin/gcc", args);

	if (removeTempC) {
		//char *rmargs[] = {"/bin/rm", "-f", tempName, NULL};
		//runcmd("/bin/rm", rmargs);
		int rem = remove(tempName);
		if (rem != 0) {
			fprintf(stderr, "Failed to remove temp file\n");
		}
	}

	return 0;
}

void runcmd(char *loc, char *args[]) {
	pid_t pid;
	int status;

	if ((pid = fork()) == -1) {
		fprintf(stderr, "Fork error.\n");
	} else if (pid == 0) {	// Child process
		execv(loc, args);
		fprintf(stderr, "Execution failure.\n");
	} else {	// Parent process
		wait(&status);
	}
}

/* Replaces things like '\n' with '\\n' */
void unspecial(char *rawstring, int lim) {
	char datacopy[lim];
	strcpy(datacopy, rawstring);

	int i, j;

	for (i=0, j=0; i < lim && datacopy[i] != '\0'; i++, j++) {
		if (j > lim) {
			fprintf(stderr, "Overflow error\n");
			break;
		} else if (datacopy[i] == '\n') {
			rawstring[j] = '\\';
			rawstring[++j] = 'n';
		} else if (datacopy[i] == '\t') {
			rawstring[j] = '\\';
			rawstring[++j] = 't';
		} else {
			rawstring[j] = datacopy[i];
		}
	}
	rawstring[j] = '\0';
}
