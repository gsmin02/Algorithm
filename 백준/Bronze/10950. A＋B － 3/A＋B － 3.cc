#include <iostream>

using namespace std;

int main() {
    int n1, s1, s2;

    cin >> n1;

    for (int i = 0; i < n1; i++) {
        cin >> s1 >> s2;
        cout << s1 + s2 << endl;
    }
    
    return 0;
}