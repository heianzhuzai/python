year = int(input("please input a year: "))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
	print("ok")
else:
	print("the year is not a leap year!")

