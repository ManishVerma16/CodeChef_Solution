def whichMixture(a, b):
	if a > 0 and b > 0:
		print('Solution')
	elif a == 0:
		print('Liquid')
	else:
		print('Solid')

	
try:
	t = int(input())
	while t>0:
		t -= 1
		a, b = map(int, input().split())
		whichMixture(a, b)
except:
	pass