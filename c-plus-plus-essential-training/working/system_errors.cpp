#include <cstdio>
#include <cerrno>

int main_system_error() {
	printf("Erasing file foo.bar\n");
	remove("foo.bar");
	printf("errno is %d\n", errno);
	perror("Can not erase file");
	return 0;
}