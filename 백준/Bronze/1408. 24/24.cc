#include <iostream>
#include <string>

using namespace std;

int main() {
	string str1, str2;

	cin >> str1 >> str2;

	int time1[3], time2[3], result[3];

	for (int i = 0; i < 3; i++) {
		time1[i] = stoi(str1.substr(i * 3, 2));
		time2[i] = stoi(str2.substr(i * 3, 2));
	}

	result[2] = time2[2] - time1[2];
	if (result[2] < 0) {
		result[2] += 60;
		time2[1]--;
	}

	result[1] = time2[1] - time1[1];
	if (result[1] < 0) {
		result[1] += 60;
		time2[0]--;
	}

	result[0] = time2[0] - time1[0];
	if (result[0] < 0) {
		result[0] += 24;
	}

	string hh = to_string(result[0]);
	string mm = to_string(result[1]);
	string ss = to_string(result[2]);

	hh = hh.length() == 1 ? '0' + hh : hh;
	mm = mm.length() == 1 ? '0' + mm : mm;
	ss = ss.length() == 1 ? '0' + ss : ss;

	cout << hh << ':' << mm << ':' << ss << endl;
}