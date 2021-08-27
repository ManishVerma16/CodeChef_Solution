def chefAndGrade(marks):
	total = sum(marks)
	avg = total//len(marks)
	if avg >= 90:
		print('O')
	elif avg < 90 and avg >= 80:
		print('A+')
	elif avg < 80 and avg >= 70:
		print('A')
	elif avg < 70 and avg >= 60:
		print('B')
	elif avg < 60 and avg >= 40:
		print('C')
	else:
		print('D')

try:
	t = int(input())
	while t>0:
		t -= 1
		n = int(input())
		marks = list(map(int, input().split()))
		chefAndGrade(marks)

except:
	pass

