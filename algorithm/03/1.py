num_temp = []
for i in range(0, 10000):
	for j in range(0, 10000):
		if j**2 == i+100:
			num_temp.append(i)

for j in range(len(num_temp)):
	for i in range(0, 10000):
		if i**2 == num_temp[j]+268:
			print(num_temp[j])

		
