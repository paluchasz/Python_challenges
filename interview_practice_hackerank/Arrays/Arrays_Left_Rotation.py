'''This program given a list and a number d moves each number in the list d inexes to the left'''
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    n = len(a)
    tempor_list = []
    tempor_list2 = []

    for i in range(d): #need to move d to the left so save the first d entries in a list
        tempor_list.append(a[i])

    for i in range(n-d): #save the remaining entries in a different temporary list
        tempor_list2.append(a[i+d])

    result = [] #then add each element to an empty list accordingly to give the result
    for number in tempor_list2:
        result.append(number)
    for number in tempor_list:
        result.append(number)

    return result

#Example: [1,2,3,4,5] with d=4, we create the list [1,2,3,4] and [5] --> [5,1,2,3,4]

    #Originally I had this but this is O(n^2) complexity and took too long
    #n = len(a)
    #for j in range(d):
    #    old_a0 = a[0]
     #   for i in range(n-1):
     #       a[i] = a[i+1]
     #   a[n-1] = old_a0
   # return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
