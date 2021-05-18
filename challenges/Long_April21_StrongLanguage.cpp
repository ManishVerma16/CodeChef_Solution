#include <iostream>
using namespace std;

int main()
{
	int t, n, k;
	cin >> t;
	while(t > 0){
		t -= 1;
		cin >> n >> k;
		char string[n];
		int count=flag=0;
	}
	return 0;
}
		for i in range(0, len(string)):
			if string[i] == '*':
				count += 1
				if count >= k:
					flag = 1
					break
			else:
				count = 0

		if flag:
			print("YES")
		else: print("NO")
		t -= 1