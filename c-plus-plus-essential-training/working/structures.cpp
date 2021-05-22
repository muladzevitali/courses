#include <cstdio>


struct S {
	int i;
	double d;
	const char* s;
};
int main_structures() {
	S s1 = { 1, 2.0, "my custom string" };
	printf("s1: %d, %f, %s\n \x5c", s1.i, s1.d, s1.s);

	return 0;
}