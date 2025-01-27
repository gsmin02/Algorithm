#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;

	for (int i = 0; i < num; i++) {
		int c, v;
		cin >> c >> v;
		cout << "You get " << c / v
			<< " piece(s) and your dad gets " << c % v
			<< " piece(s)." << endl;
	}
}