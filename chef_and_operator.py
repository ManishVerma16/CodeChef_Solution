try:
	t= int(input())
	while t>0:
		t -= 1
		x, y = map(int, input().split())
		if x < y:
			print('<')
		elif x > y:
			print('>')
		else:
			print('=')
except:
	pass