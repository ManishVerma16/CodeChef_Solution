try:
	t= int(input())
	while t>0:
		t -= 1
		c = 0
		n = input()
		for i in n:
			if i=='4':
				c += 1
		print(c)
except:
	pass