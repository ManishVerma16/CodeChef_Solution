try:
	t = int(input())
	while t>0:
		t -= 1
		g = int(input())
		while g>0:
			g -= 1
			I, N, Q=map(int, input().split())
			if N%2==0:
				print(N//2)
			else:
				if Q==I:
					print(N//2)
				else:
					print((N//2) + 1)
except:
	pass

