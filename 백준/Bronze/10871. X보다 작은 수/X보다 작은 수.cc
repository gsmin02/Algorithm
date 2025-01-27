#include <iostream>
using namespace std;

int main() {
	int n1, n2;
	int n3 = 0;

	cin >> n1 >> n2;

	int* arr1 = new int[n1];
	int* arr2 = new int[n1];

	for (int i = 0; i < n1; i++) {
		cin >> arr1[i];
	}
	for (int j = 0; j < n1; j++) {
		if (arr1[j] < n2) {
			arr2[n3] = arr1[j];
			n3++;
		}
	}
	for (int k = 0; k < n3; k++) {
		cout << arr2[k] << " ";
	}
	delete[] arr1, arr2;
	return 0;
}