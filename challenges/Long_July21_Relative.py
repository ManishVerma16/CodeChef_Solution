def relativity(g, c):
	height = int((c*c)/(2*g))
	print(height)

try:
	t = int(input())
	while t>0:
		t -= 1
		g, c = input().split()
		relativity(int(g),int(c))
except e:
	pass