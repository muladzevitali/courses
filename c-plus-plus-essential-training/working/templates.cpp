#include <iostream>

template <typename T>
T maxof(const T& a, const T& b) {
	return (a > b ? a : b);
}



int main_templates() {
	std::cout << maxof<int>(7, 9) << std::endl;
	std::cout << maxof<std::string>("valeri", "vitali") << std::endl;
	return 0;
}
