try:
	t= int(input())
	while t>0:
		t -= 1
		x, a, b = map(int,input().split())
		sugar = (a+(100-x)*b)*10
		print(sugar)
	
except:
	pass