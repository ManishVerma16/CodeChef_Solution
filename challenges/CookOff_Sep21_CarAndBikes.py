def carsAndBikes(n):
	if (n%4) == 2:
		print('YES')
	else:
		print('NO')

try:
	t = int(input())
	while t>0:
		t -= 1
		n = int(input())
		carsAndBikes(n)

except:
	pass


# try:
# 	t = int(input())
# 	while t>0:
# 		t -= 1
# 		n, p, k = map(int, input().split())
# 		res = 0

# 		x = p%k - 1
# 		y = ((n-1)//k)*k
# 		y = n-1-y

# 		if (x>y):
# 			res += (y+1)*((n-1)//k + 1) + (x-y)*((n-1)//k)
# 		else:
# 			res += ((n-1)//k + 1)*(x+1)

# 		for i in range(x+1, n, k):
# 			res += 1
# 			if(i==p):
# 				print(res)
# 				break

# except:
# 	pass



'''

def passengerBus(n, m, q):
	flag = 0
	for j in range(q):
		ch = input()
		if m >=0 :
			flag = 0
			if '+' in ch:
				m -= 1
			else:
				m += 1
		else:
			flag = 1

	if flag == 0:
		print('Consistent')
	else:
		print('Inconsistent')


special triplets

#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t>0){
	    t -= 1;
	    int n, count=0;
	    cin >>n;
	    for (int i = 1; i<=n; i++) {
	        for (int j = i; j <=n; j+=i) {
	            if(j%i==0){
	                for (int k = i; k<=n; k+=j) {
	                    if(k%j==i){
	                        count += 1;
	                    }
	                }
	            }
	        }
	    }
	    cout << count << endl;
	}
	return 0;
}



'''

