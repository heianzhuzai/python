num = int(input("Please input a number:"))
flag = 0
for i in range(1, num+1):
	for j in range(1,i+1):
		if i%j == 0:
			flag += 1
	if flag == 2:
		print(i)
	flag = 0


