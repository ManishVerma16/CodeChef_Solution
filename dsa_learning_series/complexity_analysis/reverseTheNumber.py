try:
	t = int(input())
	while t>0:
		t-=1
		n = int(input())
		r, rev = 0, 0
		while n!=0:
			r = n%10
			rev = rev*10+r
			n = n//10
		print(rev)
except:
	pass

