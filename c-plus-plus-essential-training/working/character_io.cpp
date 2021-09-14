#include <cstdio>
void unformatted_string(){
	const int buff_size = 256;
	static char buf[buff_size];
	fputs("Prompt: ", stdout);
	fgets(buf, buff_size, stdin);
	puts("Output: ");
	fputs(buf, stdout);
	fflush(stdout);
}


void formatted_string() {
	int i = 5;
	long int li = 123412343431242134L;
	const char* s = "This is the string";
	printf("integer %04d, long integer %04ld, string %s\n", i, li, s);
	printf("The pointer is %p, size is %zd\n", s, sizeof(s));
}
int main_fstrings() {
	// unformatted_string();
	formatted_string();




	return 0;
}