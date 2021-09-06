def shuffleParities(arr):
	odd_count, even_count = 0, 0
	odd, even = 0, 0
	for i in arr:
		if i%2==0:
			even_count += 1
		else:
			odd_count += 1
	if len(arr)%2 == 0:
		odd = n//2
		even = n//2
	else:
		odd = n//2 + 1
		even = n//2

	print(min(odd_count, even) + min(odd, even_count))

		


try:
	t = int(input())
	while t>0:
		t -= 1
		n = int(input())
		arr = list(map(int,input().split()))
		shuffleParities(arr)
except:
	pass




# import random
# import numpy as np


# def shuffleParities(arr):
# 	new_arr = []
# 	for i in range(len(arr)):
# 		np.random.shuffle(arr)
# 		b = [(arr[i-1] + i)%2 for i in range(1, len(arr)+1)]
# 		new_arr.append(sum(b))
# 	print(max(new_arr))