try:
	a = int(input())
	b = int(input())
	c = int(input())
	if (a>b and b>c) or (a<b and b<c):
		print(b)
	elif (b>a and a>c) or (b<a and a<c):
		print(a)
	else:
		print(c)
except:
	pass
