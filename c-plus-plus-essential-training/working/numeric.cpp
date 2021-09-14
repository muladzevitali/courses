#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>


void random_generator() {
	printf("time values: %ld\n", (long)time(nullptr));
	srand((unsigned) time(nullptr));
	// rand();

	printf("pseudo-random number %d\n", rand() % 1000);
	printf("pseudo-random number %d\n", rand() % 1000);
	printf("pseudo-random number %d\n", rand() % 1000);
	printf("RAND_MAX is %d\n", RAND_MAX);

}

int main_numeric() {
	int neg = -47;
	int x = abs(neg);
	double e = exp(1);
	double p = pow(x, 4);
	printf("x is %d\n, e is %f", x, e);
	random_generator();
	return 0;
}