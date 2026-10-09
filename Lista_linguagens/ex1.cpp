#include <iostream>

using namespace std;

int main () {
    string name;
    cout << "Digite seu nome: ";
    cin >> name;
    cout << "Olá, " << name << endl;
    return 0;
}

// Para compilar: g++ ex1.cpp -o ex1
// Para executar: ./ex1