year = int(input("Please input a year: "))
month = int(input("Please input a month: "))
day = int(input("Please input the day: "))

flag = 0
days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
	flag = 1
if month == 1:
	total = day
elif month == 2:
	total = days[1] + day
elif month == 3:
	total = days[2] + day
elif month == 4:
	total = days[3] + day
elif month == 5:
	total = days[4] + day
elif month == 6:
	total = days[5] + day
elif month == 7:
	total = days[6] + day
elif month == 8:
	total = days[7] + day
elif month == 9:
	total = days[8] + day
elif month == 10:
	total = days[9] + day
elif month == 11:
	total = days[10] + day
elif month == 12:
	total = days[11] + day
if flag == 1:
	total += 1
print("the day is the year of %d" % total)
