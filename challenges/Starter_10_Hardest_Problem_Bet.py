def hardestProblem(a, b, c):
	if c<b and c<a:
		print('Alice')
	elif b<c and b<a:
		print('Bob')
	else:
		print('Draw')
	
try:
	t = int(input())
	while t>0:
		t -= 1
		a, b, c = map(int, input().split())
		hardestProblem(a, b, c)
except:
	pass

