#include <iostream>
#include <string>
#include <vector>


int main() {
	std::cout << "Vector from initializer list" << std::endl;
	std::vector<int> vi1 = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	std::cout << "Size of vi1 " << vi1.size() << std::endl;
	std::cout << "Front of vi1 " << vi1.front() << std::endl;
	std::cout << "Back of vi1 " << vi1.back() << std::endl;
	std::cout << std::endl;

	// iterator

	std::vector<int>::iterator it_begin = vi1.begin();
	std::vector<int>::iterator it_end = vi1.end();
	for (auto i = it_begin; i < it_end; i++) {
		std::cout << *i << std::endl;
	}

	std::cout << std::endl;
	std::cout << vi1[5] << std::endl;
	return 0;
}