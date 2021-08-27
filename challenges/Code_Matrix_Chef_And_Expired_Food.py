def chefAndExpiredFood(food_packet, expired_id):
	unexpired_list = []
	for i in food_packet:
		if i not in expired_id:
			unexpired_list.append(i)

	unexpired_list.sort()
	return unexpired_list

try:
	n = int(input())
	food_packet = list(map(int, input().split()))
	m = int(input())
	expired_id = list(map(int, input().split()))
	res = chefAndExpiredFood(food_packet, expired_id)
	for i in res:
		print(i, end=' ')
except:
	pass

