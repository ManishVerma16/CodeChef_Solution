try:
	t= int(input())
	while t>0:
		t -= 1
		x, m, d = map(int,input().split())
		print(min(x*m, x+d))
except:
	pass