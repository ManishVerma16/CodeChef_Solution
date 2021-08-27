def powerOf2(arr):
	newList = []
	for i in arr:
		j = 0
		while(i- pow(2, j)>=0):
			j+=1
		j -= 1
		newList.append(i-pow(2,j))
	return newList

try:
	t = int(input())
	while t>0:
		t -= 1
		n = int(input())
		arr = list(map(int, input().split()))
		res = powerOf2(arr)
		for i in res:
			print(i, end=' ')
except:
	pass

