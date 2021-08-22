def whichDivision(rate):
	if rate >= 2000:
		print(1)
	elif rate >= 1600 and rate < 2000:
		print(2)
	else:
		print(3)


try:
	t = int(input())
	while t>0:
		t -= 1
		n = int(input())
		whichDivision(n)		

except:
	pass


