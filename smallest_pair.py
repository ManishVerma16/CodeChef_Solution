try:
	t= int(input())
	while t>0:
		t -= 1
		n = int(input())
		l = list(map(int, input().split()))
		l.sort()
		print(sum(l[0:2]))
except:
	pass