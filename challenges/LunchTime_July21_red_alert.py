def redAlert(n, d, h, arr):
	total = 0
	count = 0
	for i in arr:
		if i > 0:
			total += i
		else:
			if total < d:
				total = 0
			else:
				total -= d

		if total > h:
			count += 1

	if count > 0:
		print('YES')
	else:
		print('NO')

try:
	t = int(input())
	while t>0:
		t -= 1
		n, d, h = map(int, input().split())
		arr = list(map(int, input().split()))
		redAlert(n, d, h, arr)
except:
	pass
