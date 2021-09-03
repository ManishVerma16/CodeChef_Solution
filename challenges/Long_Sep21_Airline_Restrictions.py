try:
	t = int(input())
	while t>0:
		t -= 1
		flag = 0
		a, b, c, d, e = map(int, input().split())
		if a+b <= d and c<=e:
			flag = 1
		elif b+c <= d and a<=e:
			flag = 1
		elif a+c<= d and b<=e:
			flag =1
		else:
			flag = 0
		if flag == 1:
			print('YES')
		else:
			print('NO')
except:
	pass

