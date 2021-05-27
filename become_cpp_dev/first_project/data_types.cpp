//
// Created by muladzevitali on 23.04.21.
//
#include <iostream>

using namespace std;

struct Student {
    string name;
    float GPA;
};


class BankAccount {
private:
    float balance;
public:
    BankAccount();

    void Deposit(float);

    void WithDrawl();

    float GetBalance();

};

BankAccount::BankAccount() {
    balance = 0;
}

float BankAccount::GetBalance() {
    return balance;
}

void BankAccount::Deposit(float dep) {
    balance += dep;
}


struct Node{
    int data;
    Node *link;
};

Typedef Node* node_pointer;

int main() {
    node_pointer head;
    head = headNode;
    
}
