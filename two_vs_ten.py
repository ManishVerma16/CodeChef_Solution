try:
	t= int(input())
	while t>0:
		t -= 1
		c = 0
		x = int(input())
		if x%5==0 and x%10!=0:
			x *= 2
			c += 1
		if x%10 == 0:
			print(c)
		else:
			print(-1)
except:
	pass