"""
File: quadratic_solver.py
Name: Angus
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	print('stanCode Quadratic Solver!')
	a = float(input('輸入a值 '))
	if a == 0:
		# if a == 0 the number will be infinite
		print("error : a could not equal to 0")
	else:
		b = float(input('輸入b值 '))
		c = float(input('輸入c值 '))
		r = b*b-4*a*c
		if r < 0:
			# The negative digit could not exit in square root
			print('no real root')
		else:
			x = (-b + math.sqrt(r)) / (2 * a)
			y = (-b - math.sqrt(r)) / (2 * a)
			if r > 0:
				print('Two root'+':'+str(x)+','+str(y)+'!')
			else:
				print('One root'+':'+str(x)+'!')







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
