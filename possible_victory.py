try:
	def possibleVictory(r, o, c):
		rem_over = 20 - o
		run_socre = rem_over * 36
		if c+ run_socre > r:
			return True
		else:
			return False

	r, o, c = map(int,input().strip().split())
	res = possibleVictory(r,o,c)
	if res:
		print('Yes')
	else:
		print('No')
except:
	pass