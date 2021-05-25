#include <iostream>
#include <math.h>

using namespace std;

int main()
{
	long long int n,x,t;
	cin >> t;
	while(t--){
		cin >> n;
		x = (sqrt(8*n+1)-1)/2;
		cout << x << endl;
	}
	return 0;
}