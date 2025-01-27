#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	const int size = 1000000;
	vector<long long> arr(size + 1, 0);
	vector<long long> sum(size + 1, 0);

	for (int i = 1; i <= size; i++) {
		for (int j = i; j <= size; j += i) {
			arr[j] += i;
		}
	}

	for (int i = 1; i <= size; i++) {
		sum[i] = sum[i - 1] + arr[i];
	}

	int num;
	cin >> num;
	for (int i = 0; i < num; i++) {
		int val;
		cin >> val;
		cout << sum[val] << "\n";
	}
}