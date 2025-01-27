#include <iostream>

using namespace std;

int main() {
    int n1, n2;

    cin >> n1 >> n2;

    n2 -= 45;
    
    if(n2 < 0) {
        if (n1 == 0) {
            n1 += 23;
            n2 += 60;
        }
        else {
            n1 -= 1;
            n2 += 60;
        }
    }
    
    cout << n1 << " " << n2 << endl;
    
    
    return 0;
}