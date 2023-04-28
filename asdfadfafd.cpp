#include <iostream>
using namespace std;

class No {
public:
    int valor;
    No* prox;
    
    No(int n) {
        valor = n;
        prox = nullptr;
    }
    
    string show() {
        return to_string(valor);
    }
};

class Lista {
public:
    No* head;
    
    Lista() {
        head = nullptr;
    }
    
    void insert_inicio(No* n) {
        if (head == nullptr) {
            head = n;
        } else {
            n -> prox = head;
            head = n;
        }
    }
    
    void show() {

        cout << "***Lista***\n";
        if (head != nullptr) {
            No* temp = head;
            while (temp != nullptr) {
                cout << temp -> show() << endl;
                temp = temp -> prox;
            }
        }
    }
};

int main() {
    Lista* lista = new Lista();
    No* no1 = new No(10);
    No* no2 = new No(20);
    lista -> insert_inicio(no1);
    lista -> insert_inicio(no2);
    lista -> show();
    delete lista;
    delete no1;
    delete no2;
    return 0;
}
