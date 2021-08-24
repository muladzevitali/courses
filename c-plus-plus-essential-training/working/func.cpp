#include <cstdio>
#include "func.h"
#include <ctype.h>


int main_functions() {
	puts("This is in main()");
	// while (jump(prompt()));
	// printf("average is %lf\n", average(5, 1.0, 2.0, 34.0, 5.9, 6.1));
	unsigned long int num = 3;
	printf("factorial = %u", factorial(&num));
	return 0;
}

unsigned long int factorial(const unsigned long int *num){
	unsigned long int factorial = 1;
	for (int i = 1; i <= *num; i++) {
		factorial *= i;
	}
	return factorial;

}