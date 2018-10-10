''' Given a list of 1s and 0s we can go 1 or 2 forward. What is the shortest path
to victory given we have to avoid the 1s '''
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    moveCount = 0
    i = 0

    while i < len(c):
        if i == len(c) - 1:  #Two edge cases to fix 'index out of range issue when looking at
            break            #c[i+2]' These cases are for the last two elements of the list.
        if i == len(c) - 2:
            i += 1
            moveCount += 1
        else:
            if c[i+2] == 0: #If you can jump by two spaces then do it!
                i += 2
            else:
                i += 1
            moveCount += 1

    return moveCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
