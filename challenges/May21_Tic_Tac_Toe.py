try:
	t= int(input())
	while t>0:
		t -= 1
		countX = 0
		countO = 0
		count_ = 0

		l = []
		for i in range(3):
			tic = input()
			l.append(tic)

		for i in range(3):
			for j in range(3):
				if l[i][j] == 'X':
					countX += 1
				elif l[i][j] == 'O':
					countO += 1
				elif l[i][j] == '_':
					count_ += 1

		winX = 0 
		winO = 0

		if l[0][0] == 'X' and l[0][1] == 'X' and l[0][2] =='X':
			winX = 1
		if l[1][0] == 'X' and l[1][1] == 'X' and l[1][2] =='X':
			winX = 1
		if l[2][0] == 'X' and l[2][1] == 'X' and l[2][2] =='X':
			winX = 1
		if l[0][0] == 'X' and l[1][0] == 'X' and l[2][0] =='X':
			winX = 1
		if l[0][2] == 'X' and l[1][1] == 'X' and l[2][0] =='X':
			winX = 1
		if l[0][0] == 'X' and l[1][1] == 'X' and l[2][2] =='X':
			winX = 1
		if l[0][2] == 'X' and l[1][2] == 'X' and l[2][2] =='X':
			winX = 1
		if l[0][1] == 'X' and l[1][1] == 'X' and l[2][1] =='X':
			winX = 1

		if l[0][0] == 'O' and l[0][1] == 'O' and l[0][2] =='O':
			winO = 1
		if l[1][0] == 'O' and l[1][1] == 'O' and l[1][2] =='O':
			winO = 1
		if l[2][0] == 'O' and l[2][1] == 'O' and l[2][2] =='O':
			winO = 1
		if l[0][0] == 'O' and l[1][0] == 'O' and l[2][0] =='O':
			winO = 1
		if l[0][2] == 'O' and l[1][1] == 'O' and l[2][0] =='O':
			winO = 1
		if l[0][0] == 'O' and l[1][1] == 'O' and l[2][2] =='O':
			winO = 1
		if l[0][2] == 'O' and l[1][2] == 'O' and l[2][2] =='O':
			winO = 1
		if l[0][1] == 'O' and l[1][1] == 'O' and l[2][1] =='O':
			winO = 1

		if (winX == 1 and winO == 1) or (countX - countO < 0) or (countX - countO>1):
			print(3)
		elif countX == 0 and countO == 0 and count_ == 9:
			print(2)
		elif winX == 1 and winO == 0 and countX > countO:
			print(1)
		elif winX == 0 and winO == 1 and countX==countO:
			print(1)
		elif winX == 0 and winO == 0 and count_ == 0:
			print(1)
		elif winX == 0 and winO == 0 and count_ > 0:
			print(2)
		else:
			print(3)

except:
	pass
