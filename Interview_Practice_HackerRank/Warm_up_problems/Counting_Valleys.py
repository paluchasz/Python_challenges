'''This program has a series of Ds and Us, we start at sea level and end at sea level, we
want to find the number of valleys, ie number of times we go below sea level (and back to 0)'''
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    level = 0  #keep account of the level above/below sea level
    valleys_count = 0

    for i in range(n):
        if s[i] == "D":
            level -= 1
        if s[i] == "U":
            level += 1
        if level == -1:
            if s[i+1] == "U": #if the level is on -1 and the next thing is to go up then we know
                valleys_count += 1  #we are leaving the valley and we can add count.

    return valleys_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
