# try:
#     t = int(input())
#     for i in range(0,t):
#         string = input().lower()
#         list_char = list(string)
#         if 'm' not in list_char or 't' not in list_char:
#             print("YES")
#         elif 'g' in list_char and 't' in list_char and 'm' in list_char:
#             g = list_char.index('g')
#             t = list_char.index('t')
#             m = list_char.index('m')
#             if (g > t and g < m) or (g < t and g > m):
#                 print("YES")
#             else:
#                 print("NO")
#         else:
#             print("NO")
# except EOFError:
#     pass

# try:
#     t = int(input())
#     for i in range(0, t):
#         x, y = input().split()
#         x = int(x)
#         y = int(y)
#         minimum = x^y
#         print(minimum)
# except EOFError as e:
#     pass

'''
try:
    t = int(input())
    for i in range(0, t):
        n = int(input())
        arr = map(int, input().split())
        unique = set(arr)

except EOFError as e:
    pass

'''

'''

def maximiseFunction(arr, n):
		x = abs(arr[0]-arr[n-1])
		for i in range(0,n-1):
			if arr[i] != arr[i+1]:
				x += abs(arr[i]-arr[i+1])
		return x
try:
	t = int(input())
	while t >0:
		n = int(input())
		arr = list(map(int, input().split()))
		res = maximiseFunction(arr, n)
		print(res)
		t -= 1

except EOFError as e:
    pass

'''

'''
try:
	t = int(input())
	while t >0:
		n, k = map(int, input().split())
		while n>=k:
			n -= k
		print(n)
		t -= 1
except :
    pass

'''
'''



 
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

'''

'''
# k1 = round(k1, 1)
		# k2 = round(k2, 1)
		# k3 = round(k3, 1)
		# v = round(v, 2)
'''

'''

t = int(input())
for a in range(t):
	n = int(input())
	string = input().upper()
	j = 1
	print(f'Case #{a+1}:', end=' ')
	print(j,end =' ')
	for i in range(n-1):
		if string[i]< string[i+1]:
			j+=1
			print(j, end=' ')
		else:
			j = 1
			print(j, end=' ')
	print()

'''

'''
t = int(input())
for a in range(t):
	n = int(input())
	arr = list(map(int, input().split()))
	if n > 2:
		d = arr[0]-arr[1]
		for i in range(1, len(arr)-1):
			if arr[i]-arr[i+1] != d:
				if arr[i-1]==arr[i]:
					arr[i+1] = arr[i]
					break
				else:
					arr[i+1] = arr[i]-d
					break

		count = 1
		for i in range(0, len(arr)-1):
			if arr[i]==arr[i+1] or arr[i]>arr[i+1]:
				count += 1
			if 	arr[i]<arr[i+1]:
				count -= 1
				break
	if n == 2:
		count = 2
	print(arr)
	print(f'Case #{a+1}: {count}')
'''

'''
t = int(input())
flag = 0
min_value = []
while t>0:
	n = int(input())
	arr = list(map(int, input().split()))
	for i in range(max(arr)):
		if i not in arr:
			min_value.append(i)
			flag = 1
	if flag == 1:
		print(min(min_value))

	else: print(-1)

	t -= 1

'''



# try:
# 	t= int(input())
# 	while t>0:
# 		t -= 1
		
# except:
# 	pass

# n = int(input())
# l = pow(2, n)
# c = 0

# for x in range(l):
# 	y = x^(x+1)
# 	z = (x+2)^(x+3)
# 	if y == z:
# 		c += 1
# print(c)

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

# try:
# 	t= int(input())
# 	while t>0:
# 		t -= 1
# 		n, m = map(int, input().split())
# 		a, b = 1, 2
# 		count = 0
# 		while a<=n and b<=n:
# 			if ((m%a)%b) == ((m%b)%a):
# 				count += 1
# 			if b == n:
# 				a += 1
# 				b -= 1
# 			b += 1	
# 		print(count-1)
# except:
# 	pass

'''
try:
	t= int(input())
	while t>0:
		t -= 1
		n, m = map(int, input().split())
		count = 0
		for i in range(1, n+1):
			for j in range(i+1, n+1):
				if ((m%i)%j) == ((m%j)%i):
					count += 1
		print(count)
except:
	pass
'''



# import math
# try:
# 	a, b, c = map(int, input().split())
# 	s = (a+b+c)/2
# 	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
# 	if area:
# 		print('YES')
# 	else:
# 		print('NO')
	
# except:
# 	pass


try:
	a, b, c = map(int, input().split())
	if (a+b+c==180):
		print('YES')
	else:
		print('NO')
	
except:
	pass
