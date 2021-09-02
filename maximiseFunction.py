def maximiseFunction(arr):
		x = min(arr)
		y = max(arr)
		return (y-x)*2
try:
	t = int(input())
	while t >0:
		n = int(input())
		arr = list(map(int, input().split()))
		res = maximiseFunction(arr)
		print(res)
		t -= 1

except EOFError as e:
    pass


'''
x = abs(arr[0]-arr[n-1])
		for i in range(0,n-1):
			if arr[i] != arr[i+1]:
				x += abs(arr[i]-arr[i+1])
'''