def maxWork(d,x,y,z):
	xMax = x*7
	yzMax = y*d + (7-d)*z
	print(max(xMax, yzMax))

try:
	t = int(input())
	while t>0:
		t -= 1
		d, x, y, z = map(int, input().split())
		maxWork(d, x, y, z)
except e:
	pass