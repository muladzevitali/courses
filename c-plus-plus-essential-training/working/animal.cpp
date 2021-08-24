#include <cstdio>
#include <string>

const std::string unknown = "UNKNOWN";
const std::string clone_prefix = "clone - ";

class Animal {
	std::string type = "";
	std::string name = "";
	std::string sound = "";

public:
	Animal();
	Animal(const std::string& a_type, const std::string& a_name, const std::string& a_sound);
	Animal(const Animal& a);
	~Animal();
	Animal& operator = (const Animal&);
	void print() const;
};
Animal::Animal() : type(unknown), name(unknown), sound(unknown) {
	puts("Default constructor");
}

Animal::Animal(const std::string& a_type, const std::string& a_name, const std::string& a_sound) : type(a_type), name(a_name), sound(a_sound) {
	puts("Constructor with arguments");
}

Animal::Animal(const Animal& a) {
	puts("Constructor Copy");
	name = clone_prefix + a.name;
	type = a.type;
	sound = a.sound;
}

Animal::~Animal() {
	puts("Destructor");
	name = "";
	type = "";
	sound = "";
}

Animal& Animal::operator =(const Animal& a) {
	puts("Assignment operator");
	if (this != &a) {
		name = clone_prefix + a.name;
		type = a.type;
		sound = a.sound;
	}
	return *this;
}

void Animal::print() const{
	printf("%s the %s says %s\n", name.c_str(), type.c_str(), sound.c_str());
}


int main_animal() {
	Animal a;
	a.print();

	const Animal b("goat", "bob", "baah");
	b.print();

	Animal c = b;
	c.print();

	a = c;
	a.print();
	puts("end of main");
	
	return 0;
}