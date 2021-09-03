def travelPass(string, a, b):
	zero_count = 0
	one_count = 0
	for i in string:
		if i == '0':
			zero_count += 1
		else:
			one_count += 1

	print(zero_count*a + one_count*b)

try:
	t = int(input())
	while t>0:
		t -= 1
		n, a, b = map(int, input().split())
		string = input()
		travelPass(string, a, b)
except:
	pass

