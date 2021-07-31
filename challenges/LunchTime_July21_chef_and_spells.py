
def chefAndSpell(arr):
	total = sum(arr[1:])
	print(total)
	

try:
	t = int(input())
	while t>0:
		t -= 1
		arr = list(map(int, input().split()))
		arr.sort()
		chefAndSpell(arr)
except e:
	pass
