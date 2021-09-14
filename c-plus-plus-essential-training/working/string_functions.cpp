#include <cstdio>
#include <cstring>


const size_t max_buf = 128;
const char* s1 = "First string";
const char* s2 = "Second string";

int main_string_functions() {
	char sd1[max_buf];
	char sd2[max_buf];
	int i = 0;
	char c = 0;
	char* cp = nullptr;
	// string copy;
	strncpy(sd1, s1, max_buf);
	printf("sd1 is %s\n", sd1);
	strncpy(sd2, s2, max_buf);
	printf("sd2 is %s\n", sd2);

	// string concat
	strncat(sd1, "-", max_buf - strlen(sd1) - 1);
	printf("sd1 is %s\n", sd1);
	strncat(sd1, sd2, max_buf - strlen(sd1) - 1);
	printf("sd1 is %s\n", sd1);

	// length of strings
	printf("Length of sd1 is %zd\n", strnlen(sd1, max_buf));

	// string compare
	i = strcmp(sd1, sd2);
	printf("sd1 %s sd2, %d\n", (i == 0) ? "==" : "!=", i);
	i = strcmp(sd2, sd2);
	printf("sd2 %s sd2, %d\n", (i == 0) ? "==" : "!=", i);


	// find a character in a string;
	c = 'n';

	cp = strchr(sd1, c);
	printf("Did we find '%c' in a sd1? %s\n", c, cp ? "yes" : "no");
	if (cp) printf("The first '%c' in sd1 is at position %d\n", c, (int) (cp - sd1));

	// find a string in a string;
	cp = strstr(sd1, sd2);
	printf("Did we find '%s' in a sd1? %s\n", sd2, cp ? "yes" : "no");
	if (cp) printf("The first '%s' in sd1 is at position %d\n", sd2, (int) (cp - sd1));


	return 0;

}