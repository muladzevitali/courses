#include <iostream>
#include <math.h>
#include <ctime>

using namespace std;

int main() {
    int a = 17;
    int b = ceil(a * 1.1);
    cout << static_cast<int>(a * 1.1) << b << endl;
    cout <<  b << endl;
    cout << rand() << endl;
    const unsigned int current_time = time(0);
    srand(current_time);
    cout << current_time << endl;
    cout << rand() << endl;
}