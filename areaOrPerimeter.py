def areaOrPeri(l, b):
	peri = 2 *(l+b)
	area = l*b
	if area > peri:
		print('Area')
		print(area)
	elif area < peri:
		print('Peri')
		print(peri)
	else:
		print('Eq')
		print(area)
try:
    l = int(input())
    b = int(input())
    areaOrPeri(l, b)

except EOFError:
    pass

