#include <iostream>

using namespace std;

int main() {
	for (int i = 0; i < 3; i++) {
		int n1 = 0;
		int n2 = 0;
		for (int j = 0; j < 4; j++) {
			int num;
			cin >> num;
			if (num == 0) {
				n1++;
			}
			else if (num == 1) {
				n2++;
			}
		}
		switch (n1) {
		case 1:
			cout << "A" << endl;
			break;
		case 2:
			cout << "B" << endl;
			break;
		case 3:
			cout << "C" << endl;
			break;
		case 4:
			cout << "D" << endl;
			break;
		default:
			break;
		}
		if (n2 == 4) {
			cout << "E" << endl;
		}
	}
}