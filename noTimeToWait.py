try:
	n, h, x = map(int,input().split())
	time = list(map(int, input().split()))
	count = 0
	for i in time:
		if i+x == h:
			count += 1
			break
		# elif x == h:
		# 	count += 1
		else:
			count = 0
	if count != 0:
		print('YES')
	else:
		print('NO')
except :
	pass