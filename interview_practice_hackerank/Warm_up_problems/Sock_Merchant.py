'''This program, given a list of numbers finds the number of pairs of each number'''
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {} #initialise an empty dictionary
    d[ar[0]] = 1

    for i in range(1, n):
        if ar[i] in d:
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1

    count = 0 #number of pairs count
    for key in d:
        if d[key]%2 == 0:
            count = count + d[key]/2  #if the value is even just divide by 2 to find num of pairs
        else:
            count = count + (d[key]-1)/2  #if value is odd first subtract 1, add to count in     either case
    return int(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
