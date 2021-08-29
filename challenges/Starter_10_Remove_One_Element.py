def removeOne(a, b):
	min1 = min(a)
	max1 = max(a)
	min2 = min(b)
	max2 = max(b)
	min_value = abs(min1- min2)
	max_value = abs(max1- max2)
	print(min(min_value, max_value))
	
try:
	t = int(input())
	while t>0:
		t -= 1
		n = int(input())
		a = list(map(int, input().split()))
		b = list(map(int, input().split()))
		a.sort()
		b.sort()
		removeOne(a, b)
except:
	pass

