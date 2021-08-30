import math
try:
	t= int(input())
	while t>0:
		t -= 1
		xa, xb, Xa, Xb = map(int, input().split())
		print(Xa//xa + Xb//xb)

except:
	pass