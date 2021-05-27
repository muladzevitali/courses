//
// Created by muladzevitali on 23.04.21.
//
#include <iostream>

using namespace std;


void PrintReceipt(string, float&);

int main() {
    string company_name = "LTD 1";
    float total = 15.3;

    PrintReceipt(company_name, total);
    cout << total;
}

void PrintReceipt(string company_name, float& total) {
    cout << "Happy birthday " << company_name << endl;
    total += 1;
    cout << "You have to pay " << total << " GEL" << endl;
}
