try:
	n = int(input())
	factors = []
	count = 0
	for i in range(1, n+1):
		if n%i==0:
			count += 1
			factors.append(i)
	print(count)
	for i in factors:
		print(i, end=' ')
except:
	pass
