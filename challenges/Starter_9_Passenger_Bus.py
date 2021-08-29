def passengerBus(n, m, q):
	flag = 0
	p = 0
	# r = 0
	bus = []
	for j in range(q):
		ch = input()
		bus.append(ch)
		if m >=p and p>=0 and n>=m:
			if '+' in ch:
				p += 1
			else:
				if '+'+ch[1:] in bus:
					p -= 1
				else:
					flag = 1
		else:
			flag = 1

	if flag == 0:
		print('Consistent')
	else:
		print('Inconsistent')

try:
	t = int(input())
	while t>0:
		t -= 1
		n, m, q = map(int, input().split())
		passengerBus(n, m, q)

except:
	pass