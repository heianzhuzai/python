import math

for num in range(0, 10000):
	if ((math.sqrt(num+100))**2 == (int(math.sqrt(num+100)))**2) and ((math.sqrt(num+268))**2 == (int(math.sqrt(num+268)))**2):
		print(num)

