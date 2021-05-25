try:
	t= int(input())
	n = []
	while t>0:
		t -= 1
		x = int(input())
		n.append(x)
	n.sort()
	for i in n:
		print(i)
except:
	pass