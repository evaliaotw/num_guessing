import random
r = random.randint(1,100)
while True:
	num = input('請猜猜看，輸入一個數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		break
	elif num > r:
		print('比答案大喔!')
	else:
		print('比答案小喔!')	