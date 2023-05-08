#include <iostream>
using namespace std;

bool chk = false;

int N, mx, pre_num, stack = 0;

int main()
{
	cin >> N >> pre_num;
	int now_num;
	for (int i = 1; i < N; i++) {
		cin >> now_num;
		if (pre_num < now_num) {
			if (chk) {
				stack++;
			}
			else {
				chk = true;
				stack = 1;
			}
			if (stack > mx) {
				mx = stack;
			}
		}
		else if (pre_num > now_num) {
			if (chk) {
				chk = false;
				stack = 1;
			}
			else {
				stack++;
			}
			if (stack > mx) {
				mx = stack;
			}
		}
		pre_num = now_num;
	}
	cout << mx + 1;
	
	return 0;

}