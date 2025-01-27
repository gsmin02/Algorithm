#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    long long min, max, num, i, j;
    cin >> min >> max;

    int array[1000001] = {0, };
    int cnt = 0;

    for (i = 2; i * i <= max; i++) {
        num = (min / (i * i)) * (i * i);
        if (num < min) {
            num += (i * i);
        }
        
        for (j = num; j <= max; j += (i * i)) {
            array[j - min] = 1;
        }
    }
    
    for (int i = 0; i <= max - min; i++) {
        if (!array[i]) {
            cnt++;
        }
    }

    cout << cnt;

    return 0;
}