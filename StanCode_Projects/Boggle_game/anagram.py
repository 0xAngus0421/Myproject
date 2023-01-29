"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_list = []

def main():
    """
    TODO:
    """
    print("Welcome to stanCode \"Anagram Generator\" (or " + str(EXIT) + " to quit)")

    while True:
        s = input('Find anagram for:')
        if s == EXIT:
            break
        start = time.time()
        read_dictionary()
        ans = []
        find_anagrams(s,ans)
        print(f'{len(ans)} anagrams: {ans}')


        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE,'r') as f:
        for line in f:
            word_list.append(line.strip())



def find_anagrams(s,ans):
    """
    :param s:
    :return:
    """
    print('Searching...')
    find_anagrams_helper(s,ans,'',[])


def find_anagrams_helper(s,ans,string,index):
    if len(string) == len(s):
        if string in word_list and string not in ans:
            ans.append(string)
            print('Found: ' + string)
            print('Searching...')
    else:
        for i in range(len(s)):
            if i not in index:
                index.append(i)
                string += s[i]

                if has_prefix(string):
                    find_anagrams_helper(s, ans, string,index)

                string = string[:-1]
                index.pop()












def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in word_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
