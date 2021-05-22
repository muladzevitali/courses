#include <cstdio>


struct Prefs {
	bool likes_music : 1;
	bool has_hair : 1;
	bool has_internet : 1;
	bool has_dinosaur : 1;
	unsigned int number_of_children : 4;
};


int main_bit_fields() {
	Prefs homer;
	homer.likes_music = true;
	homer.has_hair = true;
	homer.has_internet = true;
	homer.has_dinosaur = false;
	homer.number_of_children = 0;
	printf("Size of homer: %d\n", sizeof(homer) * 8);

	if (homer.likes_music) printf("homer likes music\n");
	if (homer.has_hair) printf("homer has hair\n");
	if (homer.has_internet) printf("homer has internet\n");
	if (homer.has_dinosaur) printf("homer has dinosaur\n");
	printf("homer has %d children\n", homer.number_of_children);


	return 0;
}