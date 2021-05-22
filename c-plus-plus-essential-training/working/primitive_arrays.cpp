#include <cstdio>

int main_primitive_arrays() {
	int array[5] = { 1, 2, 4, 4, 5 };
	array[3] = 13;
	for (int i : array) {
		printf("%d\n", i);
	}
	int* array_pointer = array;
	printf("%d\n", *array_pointer);
	
	++array_pointer;
	printf(" new %d\n", *array_pointer);
	*array_pointer = 127;
	printf(" new new %d\n", *array_pointer);

	puts("");

	return 0;
}