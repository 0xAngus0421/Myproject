"""
File: weather_master.py
Name: Angus
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def cold_day(s):
	s += 1
	return s


def total(y):
	y += 1
	return y


def main():
	print("SC001\"Weather Master\"4.0!!!")
	data = int(input('Next Temperature: (or  ' + str(EXIT) + '  to quit)?  '))
	if data == EXIT:
		print('No Temperature were entered')
	else:
		maximum = data
		minimum = data
		s = 0
		# calculate the days of temperature under 16
		y = 0
		# calculate the total data number
		c = data
		while True:
			y = total(y)
			if data < 16 and data != EXIT:
				s = cold_day(s)
			data = int(input('Next Temperature: (or  ' + str(EXIT) + '  to quit)?  '))
			# the constant need to put behind this code
			if data != EXIT:
				c = c + data
			if data == EXIT:
				break
			if maximum < data:
				maximum = data
			if minimum > data:
				minimum = data

		print('Highest Temperature:' + str(maximum))
		print('Lowest Temperature:' + str(minimum))
		print('Average '+str(c/y))
		print(str(s)+' cold day(s)')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
