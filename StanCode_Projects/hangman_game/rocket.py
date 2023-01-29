"""
File: rocket.py
Name: Angus
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3

def head():
	for i in range(SIZE):
		for a in range(SIZE-i):
			print(' ', end="")
		for b in range(i+1):
			print('/', end="")
		for j in range(i+1):
			print('\\', end="")
		print("")


def belt():
	for i in range(1):
		print('+', end="")
		for j in range(SIZE*2):
			print('=', end="")
		print('+', end="")
		print("")

def upper():
	for i in range(SIZE):
		print('|', end="")
		for a in range(SIZE-1-i):
			print('.', end="")
		for b in range(i+1):
			print('/\\', end="")
		for c in range(SIZE-1-i):
			print('.', end="")
		print('|', end="")
		print("")

def lower():
	for i in range(SIZE):
		print('|', end="")
		for a in range(i):
			print('.', end="")
		for b in range(SIZE-i):
			print('\\/', end="")
		for c in range(i):
			print('.', end="")
		print('|', end="")
		print("")


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()