# Actual solution

def interestingXOR(c):
	x = c
	d = 0
	while x>0:
		d += 1
		x = x//2
	a = pow(2, d-1)-1
	b = a^c
	print(a,b)
	return a*b

try:
	t = int(input())
	while t>0:
		c = int(input())
		print(interestingXOR(c))
		t -= 1
except:
	pass

# Brute force approach to find all possible pairs
# O(n^2)
def interestingXOR(c):
	x = c
	d = 0
	while x>0:
		d += 1
		x = x//2
	max_product = []
	for i in range(1, pow(2, d)):
		for j in range(i,pow(2, d)):
			if c == i^j and i != j:
				max_product.append(i*j)
	print(max_product, max(max_product))

try:
	t = int(input())
	while t>0:
			
		c = int(input())
		print(interestingXOR(c))
		t -= 1
except:
	pass

# O(n)
def interestingXOR(c):
	x = 0
	max_product = []
	if c > 1:
		for i in range(1,c):
			x = c^i
			max_product.append(x*i)
			print(i, x)
		return max(max_product)
	else:
		return c

try:
	t = int(input())
	while t>0:
			
		c = int(input())
		print(interestingXOR(c))
		t -= 1
except:
	pass




