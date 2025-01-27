#include <iostream>

using namespace std;

int main() {
	int n, m;
	cin >> m >> n;

	int min = 0;
	int sum = 0;

	int i = 0;

	while (i * i <= n) {
		if (i * i >= m) {
			sum += i * i;
			if (min == 0) {
				min = i * i;
			}
		}
		i++;
	}

	if (sum == 0) {
		cout << -1 << endl;
	}
	else {
		cout << sum << '\n' << min << endl;
	}

}