try:
	a, b, c = map(int, input().split())
	if (a==b and b==c and a==c) and (a+b>c and b+c>a and a+c>b):
		print(1)
	elif (a==b or b==c or a==c) and (a+b>c and b+c>a and a+c>b):
		print(2)
	elif (a!=b or b!=c or a!=c) and (a+b>c and b+c>a and a+c>b):
		print(3)
	else:
		print(-1)
	
except:
	pass
