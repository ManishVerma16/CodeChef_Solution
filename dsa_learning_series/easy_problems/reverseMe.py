try:
	n = int(input())
	num = list(map(int, input().split()))

	for i in num[::-1]:
		print(i, end=' ')
	
except:
	pass
