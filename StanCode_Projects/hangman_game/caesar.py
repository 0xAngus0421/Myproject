"""
File: caesar.py
Name: Angus
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    """
    data = int(input('Secret number:'))
    ciphered_string = input("What's the ciphered string?")
    ciphered_string = ciphered_string.upper()
    y = caesar_decipher(ciphered_string, data)
    print('The deciphered string is '+y)


def caesar_decipher(ciphered_string, data):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_alphabet = alphabet[26-data:]+alphabet[:26-data]
    ans = ""
    for i in range(len(ciphered_string)):
        ch = ciphered_string[i]
        r = new_alphabet.find(ch.upper())
        # case insensitive
        if r == -1:
            ans += ch
        else:
            ans += alphabet[r]
    return ans



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
