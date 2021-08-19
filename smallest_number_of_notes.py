def smallestNumberOfNotes(n):
	count = 0
	while n>0:
		if n>=100:
			n -= 100
			count += 1
		elif n>=50:
			n -= 50
			count += 1
		elif n>=10:
			n -= 10
			count += 1
		elif n>=5:
			n -= 5
			count += 1
		elif n>=2:
			n -= 2
			count += 1
		else:
			n -= 1
			count += 1
	return count


try:
    t = int(input())
    while t>0:
    	t -= 1
    	n = int(input())
    	res = smallestNumberOfNotes(n)
    	print(res)
except:
    pass
