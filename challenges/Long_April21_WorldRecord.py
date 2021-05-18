# World Record Bolt
try:
	t=int(input())
	while t>0:
		t -= 1	
		k1, k2, k3, v = map(float, input().strip().split())
		totalSpeed = k1*k2*k3*v
		time = round(100.00/totalSpeed, 2)
		if time>=9.58:
			print("NO")
		else:	print("YES")
except :
	pass


