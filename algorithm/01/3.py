flag = 0
num_flag = 0
for num in range(111, 445):
	num_temp = str(num)
	for i in range(3):
		if num_temp[i] == '0' or num_temp[i] >= '5':
			flag += 1	
	if flag > 0:
		flag = 0
		continue
	else:
		if (num_temp[0] != num_temp[1]) and (num_temp[0] != num_temp[2]) and (num_temp[1] != num_temp[2]):
			num_flag += 1
			print(num_temp)
print("num = %d" %num_flag)



