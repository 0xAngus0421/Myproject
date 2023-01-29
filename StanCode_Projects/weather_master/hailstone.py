"""
File: hailstone.py
Name: Angus
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
EXIT = 1


def my_number(x):
    if x % 2 == 1:
        n = 3 * x + 1
        print(str(x) + '  is odd , so I make 3n+1 : ' + str(n))
        return n
    elif x % 2 == 0:
        n = x / 2
        print(str(x) + '  is even , so I take half : ' + str(n))
        return n


def step_plus_one(s):
    s += 1
    return s


def main():
    print('This program computes Hailstone sequence')
    x = int(input('Please key in  the first number!'))
    s = 0
    if x == EXIT:
        pass
    if x <= 0:
        print('Invalid number please key in positive number')
    else:
        while x > 0 and x != 1:
            x = my_number(x)
            s = step_plus_one(s)
        print('It took  '+str(s)+'  steps to reach 1')




















###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
