#include <iostream>

using namespace std;

int main() {
    int n1;
    cin >> n1;

    for (int i = 0; i < n1; i++) {
        for (int j = 0; j < i; j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * (n1 - i) - 1; j++) {
            cout << "*";
        }
        cout << "\n";
    }
    for (int i = 0; i < n1 - 1; i++) {
        for (int j = 0; j < n1 - i - 2; j++) {
            cout << " ";
        }
        for (int j = 0; j < 2 * (i + 1) + 1; j++) {
            cout << "*";
        }
        cout << "\n";
    }

}