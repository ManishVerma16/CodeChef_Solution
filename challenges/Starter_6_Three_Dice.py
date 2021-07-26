def threeDice(x, y):
	prob = 6-(x+y)
	if prob <= 0:
		print(0)
	else:
		print(round(prob/6, 6))

try:
	t = int(input())
	while t>0:
		t -= 1
		x, y= map(int, input().split())
		threeDice(x, y)
except e:
	pass
