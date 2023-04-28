#include <iostream>
using namespace std;

class Obj {
    public:
        int valor;
        Obj* prox;

        Obj(int x) {
            valor = x;
            prox = nullptr;
        }
    
    string show() {
        return to_string(valor); 
    }
};

class LinkedList {
    public:
        Obj* head;

        LinkedList(Obj* head x) {
            if (head == nullptr) {
                head = x;
            } else {
                x -> prox = head;
                head = x;
            }
        }
}

int Count() {
    for() {
        
    }
}
