//
// Created by muladzevitali on 23.04.21.
//

#include <iostream>
#include <fstream>

using namespace std;

int ReadFile();
void WriteInFile();

int main(){
    WriteInFile();
}

int ReadFile(){
    ifstream input_stream;
    string some_text;

    input_stream.open("/home/muladzevitali/Projects/cpp_learning_path/become_cpp_dev/first_project/text.txt");
    if(input_stream.fail()){
        cout << "Couldn't open the file" << endl;

        return 0;
    }
    while(input_stream >> some_text){
        cout << "Text is: " << some_text << endl;
    }

    input_stream.close();
    return 1;
}

void WriteInFile(){
    ofstream output_stream;

    output_stream.open("some.txt", ios::app);
    output_stream << "Charles " << 20 << endl;
    output_stream.close();
}