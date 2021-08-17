def largeSquare(n,a):
	print(int(n**0.5)*a)

try:
	t = int(input())
	while t>0:
		t -= 1
		n, a = map(int, input().split())
		largeSquare(n,a)
except:
	pass