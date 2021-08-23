try:
	t= int(input())
	while t>0:
		t -= 1
		n, m = map(int, input().split())
		count = 0
		for i in range(1, n+1):
			for j in range(i+1, n+1):
				if ((m%i)%j) == ((m%j)%i):
					count += 1
		print(count)
except:
	pass