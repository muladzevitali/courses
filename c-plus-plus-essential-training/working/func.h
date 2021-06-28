#include <ctype.h>
#include <cstdarg>


void fa() {
	puts("This is fa()");
}
void fb() {
	puts("This is fb()");
}
void fc() {
	puts("This is fc()");
}
void fd() {
	puts("This is fd()");
}

void (*funcs[])() = { fa, fb, fc, fd };

const char* prompt() {
	puts("Choose an option:");
	puts("1. Function fa()");
	puts("2. Function fb()");
	puts("3. Function fc()");
	puts("4. Function fd()");
	puts("Q. Quit.");

	printf(">>");
	fflush(stdout);

	const int buff_size = 16;
	static char response[buff_size];
	fgets(response, buff_size, stdin);

	return response;
}

int jump(const char* rs) {
	char code = rs[0];

	printf("Code: %d\n", code);
	if (toupper(code) == 'Q') { return 0; }
	size_t func_length = sizeof(funcs) / sizeof(funcs[0]);

	size_t i = (size_t)code - '0';
	if ( i < 1 || i > func_length) {
		puts("Invalid choice");
		return 1;
	}
	funcs[i - 1]();
	return 1;

}

double average(const int count, ...) {
	va_list ap;
	int i;
	double total = 0.0;
	va_start(ap, count);
	for (i = 0; i < count; i++) {
		total += va_arg(ap, double);
	}
	va_end(ap);
	return total / count;
}
unsigned long int factorial(const unsigned long int* num);
