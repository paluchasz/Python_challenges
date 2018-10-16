'''This program given a 2D array finds all hourglasses (turned over H shape) and
finds the largest sum of each hourglass' elements.'''
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    largest_sum = -100 #lowest possible is actually -9*7 = -63 so we can be safe with 100 to compare

    for i in range(4):
        for j in range(4):
            hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] #i represents the row, j the column!
            if hourglass_sum > largest_sum:
                largest_sum = hourglass_sum

    return largest_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
