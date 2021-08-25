#SpaceArray

def spaceArray(arr, n):
	perm = list(range(1,n+1))
	i = 0
	flag = 0
	while i<n:
		if (arr[i] <= perm[i]):
			flag += abs(perm[i]-arr[i])
		else:
			flag = 0
			break
		i += 1
	if flag%2 != 0:
		print('First')
	else:
		print('Second')

try:
	t = int(input())
	while t > 0:
		n = int(input())
		arr = list(map(int, input().split()))
		arr.sort()
		spaceArray(arr,n)
		t -= 1
except :
	pass

