'''In this question given a list we have to find how many swaps it took from
the original list [1,2,3...] with the constraint that each number could only have
moved by at most 2 places'''
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    current_swaps = True

    while current_swaps:

        current_swaps = False
        for i in range(len(q)-1):

            if q[i] > i + 3:
                return "Too chaotic"


            if q[i] > q[i+1]:
                current = q[i]
                q[i] = q[i+1]
                q[i+1] = current
                current_swaps = True
                swaps += 1

    return swaps



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        result = minimumBribes(q)

        print(result)
