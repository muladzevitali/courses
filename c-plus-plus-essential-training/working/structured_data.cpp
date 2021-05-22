#include <cstdio>


struct Employee {
	int id;
	const char* name;
	const char* role;
};


int main_structured_data() {
	// can ommit struct
	struct Employee joe = { 1, "Joe", "CTO" };
	Employee* j = &joe;

	printf("ID: %d, NAME: %s, ROLE: %s\n", joe.id, joe.name, joe.role);
	printf("ID: %d, NAME: %s, ROLE: %s", j -> id, j -> name, j -> role);
	return 0;
}