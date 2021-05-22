#include <cstdio>


int main_type_cast() {

	int x = 4;
	long long int y;
	y = x;

	x = (int)y;

	size_t z = sizeof x;
	size_t n = sizeof(int);
	printf("size of x is %zd\n", z);
	printf("size of int is %zd\n", n);

	return 0;
}