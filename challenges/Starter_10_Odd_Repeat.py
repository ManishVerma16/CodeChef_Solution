def oddRepeat(n, k, s):
	diff = s - n**2
	num = diff//(k-1)
	print(num)
	
	
try:
	t = int(input())
	while t>0:
		t -= 1
		n, k, s = map(int, input().split())
		oddRepeat(n, k, s)
except:
	pass

