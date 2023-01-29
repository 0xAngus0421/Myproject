"""
File: similarity.py
Name: Angus
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def similarity(dna, dna2):
    final_ans = ""
    final_count = 0
    for i in range(len(dna)-len(dna2)+1):
        ans = ""
        count = 0
        # calculate the match rate
        for j in range(len(dna2)):
            ans += dna[i + j]
            ch = dna2[j]
            if ch not in dna:
                return 'error'
            elif ch == dna[i+j]:
                count += 1
        if count >= final_count:
            # store the data in blank
            final_count = count
            final_ans = ans
    return final_ans




















def main():
    """
    TODO:
    """
    dna = input("Please give me a DNA sequence to search: ")
    dna = dna.upper()
    dna2 = input('What DNA sequence would you like to match: ')
    dna2 = dna2.upper()
    s = similarity(dna, dna2)
    print('The best match is '+s)

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
