def threeBoxes(a, b, c, d):
	if a+b+c <= d:
		print(1)
	elif c + a <= d or a+b<=d:
		print(2)
	else:
		print(3)

	
try:
	t = int(input())
	while t>0:
		t -= 1
		a, b, c, d = map(int, input().split())
		threeBoxes(a, b, c, d)
except:
	pass

'''

total = a+b+c
	if total <= d:
		print(1)
	elif total%d == 0:
		print(int(total/d))
	else:
		print(int(total/d)+1)
'''