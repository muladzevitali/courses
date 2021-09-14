#include <cstdio>
#include <typeinfo>

struct A {
	int x;
};

struct B {
	int x;
};

A a1;
A a2;
B b1;
B b2;


int type_id() {
	if (typeid(a1) == typeid(A)) {
		puts("same");
	}
	else {
		puts("different");
	}
	return 0;
} 