try:
	def noblePrize(courses, m):
		uniqueCourse = len(set(courses))
		return uniqueCourse<m

	t = int(input())
	while t>0:
		t -= 1
		n, m = map(int, input().strip().split())
		courses = list(map(int, input().strip().split()))
		res = noblePrize(courses,m)
		if res:
			print('Yes')
		else:
			print('No')
except :
	pass