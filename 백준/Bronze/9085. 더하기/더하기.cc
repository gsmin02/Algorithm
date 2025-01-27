#include <iostream>

using namespace std;

int main() {
	int n1;
	cin >> n1;
	for (int i = 0; i < n1; i++) {
		int n2;
		cin >> n2;
		int result = 0;

		for (int j = 0; j < n2; j++) {
			int n3;
			cin >> n3;
			if (n3 <= 10) {
				result += n3;
			}
		}
		cout << result << endl;
	}
}