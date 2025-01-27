#include <iostream>
#include <string>

using namespace std;

int main() {
	string str;
	int n, m;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> m >> str;
		for (int j = 0; j < str.length(); j++) {
			for (int k = 0; k < m; k++) {
				cout << str[j];
			}
		}
		cout << "\n";
	}

	return 0;
}