try:
	n, k = map(int, input().split())
	num = list(map(int, input().split()))
	if k in num:
		print(1)
	else:
		print(-1)
	
except:
	pass