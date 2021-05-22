#include <cstdio>
#include <new>


const long int COUNT = 1024000;


int main_dynamic_memory_operations() {
	long int* ip;

	try {
		ip = new long int[COUNT];

	}
	catch (std::bad_alloc& ba){
		fprintf(stderr, "Cann't allocate memory (%s)\n", ba.what());
		return 1;
	}

	for (long int i = 0; i < COUNT; i++) {
		ip[i] = i;
	}

	delete[] ip;
	return 0;
}