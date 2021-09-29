def playOffs(x, y, z):
	qualify = False
	rem_points = y - x
	if rem_points <= z*2:
		qualify = True
	elif rem_points <= z*1:
		qualify = True
	else:
		qualify = False

	if qualify == True:
		print('YES')
	else:
		print('NO')
	
try:
	t = int(input())
	while t>0:
		t -= 1
		x, y, z = map(int, input().split())
		playOffs(x, y, z)
except:
	pass


'''
def playOffs(x, y, z):
	if z*2 + x >= y:
		print('YES')
	else:
		print('NO')
	
try:
	t = int(input())
	while t>0:
		t -= 1
		x, y, z = map(int, input().split())
		playOffs(x, y, z)
except:
	pass

'''

