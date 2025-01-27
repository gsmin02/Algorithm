#include <iostream>
#include <string>

using namespace std;

int main() {
	int n;
	int sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		char m;
		cin >> m;
		int j = m;
		sum += j - 48;
	}
	cout << sum << endl;

	return 0;
}