#include <cstdio>


int main_fm() {
	static const char* file_name = "file";
	static const char* file_new_name = "new_file";
	// FILE* output_stream = fopen(file_name, "w");

	//fclose(output_stream);
	rename(file_name, file_new_name);
	remove(file_new_name);

	return 0;
}
