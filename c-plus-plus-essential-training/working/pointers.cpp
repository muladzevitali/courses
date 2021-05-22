#include <cstdio>

int main_pointers() {
	int x = 12;
	int* ip = &x;
	printf("x is %d\n", x);
	printf("ip is %d\n", *ip);
	

	x = 15;
	printf("ip is %d\n", *ip);

	return 0;
}