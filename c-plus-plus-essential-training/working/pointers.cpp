#include <cstdio>

int main_pints() {
	int x[3] = { 12, 13, 14 };
	int* ip = x;
	printf("x is %p\n", &x[0]);
	printf("ip is %p\n", ip);
	

	printf("*ip++ = %d\n", *ip++);
	printf("x[0] = %d\n", x[0]);
	printf("ip = %p\n", ip);

	printf("*++ip = %d\n", *++ip);
	printf("x[2] = %d\n", x[2]);
	printf("ip = %p\n", ip);

	return 0;
}