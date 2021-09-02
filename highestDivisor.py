def highestDivisor(n):
	arr = []
	for i in range(1, n+1):
		if n%i ==0 and (i>=1 and i <=10):
			arr.append(i)
	return max(arr)



n = int(input())
res = highestDivisor(n)
print(res)