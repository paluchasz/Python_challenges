'''We are given a string and a number n. We want to concantate the string until we
get a string of desired length n and find the number of a's in that string '''
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    letter_a_count = 0

    for letter in s:
        if letter == "a":
            letter_a_count += 1 #find the number of a's in one repetition of string

    r = n%len(s) #r the remainder of when we divide n by the length of string
    number_of_full_strings = int((n-r)/len(s))
    #e.g is string is abcd and n=10 we have abcd * 2 and left over ab

    left_over_a_count = 0

    for i in range(r):
        if s[i] == "a":
            left_over_a_count += 1

    letter_a_count = number_of_full_strings*letter_a_count + left_over_a_count

    return letter_a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
