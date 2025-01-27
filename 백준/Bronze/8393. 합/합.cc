#include <iostream>

using namespace std;

int main() {
    int n1, s1 = 0;

    cin >> n1;

    for (int i = 1; i <= n1; i++)
        s1 += i;
    
    cout << s1 << endl;
    
    return 0;
}