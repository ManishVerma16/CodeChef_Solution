try:
	n = int(input())
	maxPrice = []
	priceList = []
	while n>0:
		priceList.append(int(input()))
		n-=1
	priceList.sort()
	for i in range(len(priceList)):
		maxPrice.append(priceList[i]*(len(priceList)-i))
	print(max(maxPrice))
except:
	pass

