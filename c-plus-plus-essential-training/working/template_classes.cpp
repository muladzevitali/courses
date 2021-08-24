#include<iostream>
#include<string>
#include<exception>

class BWex : public std::exception {
	const char* msg;
	BWex();
public:
	explicit BWex(const char* s) throw() :msg(s) {};
	const char* what() const throw() { return msg; };

};

template <typename T>
class Stack {
	static const int default_size = 10;
	static const int max_size = 1000;
	int s_size;
	int s_top;
	T* stack_ptr;
public:
	explicit Stack(int s = default_size);
	~Stack() { if (stack_ptr) delete[] stack_ptr; };
	T& push(const T& i);
	T& pop();
	bool is_empty() const { return s_top < 0; }
	bool is_full() const { return s_top >= s_size - 1; }
	int top() const { return s_top; }
	int size() const { return s_size; }
};

template <typename T>
Stack<T>::Stack(int s) {
	if (s > max_size || s < 1) throw BWex("invalid stack size");
	else s_size = s;
	stack_ptr = new T[s_size];
	s_top = -1;
}

template <typename T>
T& Stack<T>::push(const T& i) {
	if (is_full()) throw BWex("stack full");
	return stack_ptr[++s_top] = i;
}
template <typename T>
T& Stack<T>::pop() {
	if (is_empty()) throw BWex("stack empty");
	return stack_ptr[s_top--];
}

int main_templace_classes() {
	Stack<int> st(5);
	std::cout << "stack size " << st.size() << std::endl;
	std::cout << "stack top " << st.top() << std::endl;

	for (int i : { 1, 2, 3, 4, 5 }) {
		st.push(i);
	}

	std::cout << "stack size after push " << st.size() << std::endl;
	std::cout << "stack top after push " << st.size() << std::endl;
	std::cout << "stack is full? " << st.is_full() << std::endl;
	while (!st.is_empty()) {
		std::cout << "popped " << st.pop() << std::endl;
	}

	std::cout << "stack is empty? " << st.is_empty() << std::endl;
	return 0;

}


