#include <cstdio>

constexpr int max_string = 1024;
constexpr int repeat = 5;

int main_str_io() {
	const char* fn = "test.txt";
	const char* string = "This is what is inside.\n";
	puts("Writing in file");
	FILE* fw = fopen(fn, "w");
	for (int i = 0; i < repeat; i++) {
		fputs(string, fw);
	}
	fclose(fw);
	puts("Done");

	puts("Reading file");
	char buf[max_string];
	FILE* fr = fopen(fn, "r");
	while (fgets(buf, max_string, fr)) {
		fputs(buf, stdout);
	}
	fclose(fr);
	remove(fn);
	puts("Done");
	return 0;
}