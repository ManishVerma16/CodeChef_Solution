# Causing TLE
# try:
# 	t= int(input())
# 	while t>0:
# 		t -= 1
# 		n = int(input())
# 		mod = 1000000007
# 		x = pow(2, n-1)%mod
# 		print(x)
# except:
# 	pass

try:
	t= int(input())
	while t>0:
		t -= 1
		n = int(input())
		x = 2
		y = n-1
		z = 1
		mod = 1000000007
		while y > 0:
			if y%2 == 1:
				z = (z*x)%mod
			x = (x*x)%mod
			y //= 2
		print(z)
except:
	pass
