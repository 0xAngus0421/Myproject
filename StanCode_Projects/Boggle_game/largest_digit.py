"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if abs(n)/10 < 1:#代表只有他自己
		return abs(n)
	else:
		r = abs(n) % 10 #取餘數就是最後一個數字(由右到左)
		if r > find_largest_digit(abs(n)//10):
			return r
		else:
			return find_largest_digit(abs(n)//10)




if __name__ == '__main__':
	main()
