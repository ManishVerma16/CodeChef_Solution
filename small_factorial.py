try:
	t= int(input())
	while t>0:
		t -= 1
		f = 1
		n = int(input())
		for i in range(1,n+1):
			f *= i
		print(f)
except:
	pass