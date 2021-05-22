#include <cstdio>

// recommended to have const int& because of side effects
int& func(int& i);

int main_references() {
	int i = 12;
	// cann't change, unreference, create without initialization
	int& ir = i;

	ir = 13;

	printf("i is %d\n", i);
	func(i);

	printf("i is %d\n", i);
	
	func(i) = 1234;
	printf("i is %d\n", i);
	return 0;
}

int& func(int& i) {
	return ++i;
}