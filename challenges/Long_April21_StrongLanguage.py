# Strong Language
try:
	t = int(input())
	while t>0:
		n, k = map(int, input().split())
		string = input().lower()
		count, flag = 0, 0
		for i in range(0, len(string)):
			if string[i] == '*':
				count += 1
				if count >= k:
					flag = 1
					break
			else:
				count = 0

		if flag:
			print("YES")
		else: print("NO")
		t -= 1
except :
	pass