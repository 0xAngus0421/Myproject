"""
File: hangman.py
Name: Angus
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    h = N_TURNS
    answer = random_word()
    final_answer = '_' * len(answer)
    while h > 0:
        print('The word looks like:'+str(final_answer))
        print("You have " + str(h) + '  guesses left')
        data = input("Your guesses")
        data = data.upper()
        if data.isalpha() and len(data) == 1:
            # distinguish the data whether follow rules
            if data not in answer:
                h = h - 1
                print("There is no  " + data + "'s  " + 'in the word')
                if h == 0:
                    print("You are completely hung : (")
                    print('The word was: ' + answer)
                    break
            for i in range(len(answer)):
                if answer[i] in data:
                    # we could know the data whether in answer and show it
                    final_answer = final_answer[:i] + answer[i] + final_answer[i+1:]

            if final_answer == answer:
                print('You win !')
                print('The word was: '+answer)
                break
        else:
            print('illegal format')





def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
