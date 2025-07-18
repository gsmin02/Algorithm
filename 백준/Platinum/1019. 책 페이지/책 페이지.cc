#include <iostream>
using namespace std;

int main() {

    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int n; cin >> n;
    int chk[10] = {0,};
    int i;
    int ten = 1;
    int cnt = 0;
    int r;

    while (n > 0)
    {
        r = n%10;
        n /= 10;

        for (i=0; i<r; i++) chk[i] += ten*(n+1);
        for (i=r+1; i<10; i++) chk[i] += ten*n;
        chk[r] += ten*n + cnt + 1;
        chk[0] -= ten;
        cnt += ten*r;

        ten *= 10;
    }

    for (i=0; i<10; i++) cout << chk[i] << ' ';
    
}