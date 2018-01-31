for i in range(1, 5):
	for j in range(1, 5):
		for z in range(1, 5):
			num = str(i) + str(j) + str(z)
			if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]:
				print(num)
