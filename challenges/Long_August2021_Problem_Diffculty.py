def beautifulPairs(arr):
	unique = set(arr)
	if len(unique) == 3 or len(unique) == 4:
		print(2)
	elif len(unique) == 2 and (arr.count(arr[0])==2 or arr.count(arr[1])==2):
		print(2)
	elif len(unique) == 2:
		print(1)
	else:
		print(0)
	

try:
	t = int(input())
	while t>0:
		t -= 1
		arr = list(map(int, input().split()))
		beautifulPairs(arr)

except:
	pass


'''
logic 

len of array or set => 4 or 3 (unique values)  => 2 set  
test values : 5 3 2 1, 3 2 2 1

len of array or set => 2 (unique values with their count as 2)  => 2 set
test values : 2 1 2 1, 3 2 2 3

len of array or set=> 2 (unique values)  => 1 set
test values : 5 3 3 3 

len of array or set => 1 (unique value) => 0 set
test values : 2 2 2 2


'''