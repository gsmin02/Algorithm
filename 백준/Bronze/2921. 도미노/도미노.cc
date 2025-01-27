#include <iostream>

using namespace std;

int main() {
	int num;
	cin >> num;

	int result = 0;

	for (int i = 0; i <= num; ++i)
		for (int j = i; j <= num; ++j)
			result += i + j;

	cout << result;
}