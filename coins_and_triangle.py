import math
try:
	t= int(input())
	while t>0:
		t -= 1
		n = int(input())
		x = int((math.sqrt(8*n+1)-1)/2)
		print(x)
except:
	pass