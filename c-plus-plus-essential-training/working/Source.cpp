#include <cstdio>

int main_old() {
	int x;
	x = 42;

	printf("x is %d\n", x);
	printf("x is %d\n", x = 43);

	return 0;
}