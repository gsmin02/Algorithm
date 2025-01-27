#include <iostream>

using namespace std;

int main() {
    int n1;

    cin.tie(NULL);
    cin.sync_with_stdio(false);

    cin >> n1;

    for (int i = 0; i < n1; i++) {
        for (int k = n1 - i; k > 1; k--) {
            cout << " ";
        }
        for (int j = 0; j <= i*2; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}