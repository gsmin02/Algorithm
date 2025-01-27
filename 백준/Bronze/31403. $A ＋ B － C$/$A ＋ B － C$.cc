#include <iostream>
#include <string>

using namespace std;

int main() {
	int n1, n2, n3;
	string s1, s2, s3;

	cin >> s1 >> s2>> n3;

	n1 = stoi(s1);
	n2 = stoi(s2);

	s3 = s1 + s2;

	cout << n1 + n2 - n3 << endl;
	cout << stoi(s3) - n3 << endl;
}