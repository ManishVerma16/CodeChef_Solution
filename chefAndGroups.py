def chefAndGroups(arr):
	count = 0
	for i in range(len(arr)-1):
		if arr[i] != arr[i+1]:
			count += 1
	if arr[0] == '0' and arr[-1]=='0':
		return count//2
	else:
		return (count//2) + 1
try:
	t = int(input())
	while t>0:
		s = list(input())
		print(chefAndGroups(s))
		t -= 1
except :
	pass

