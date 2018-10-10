# Note this is the code that worked for hackerrank, ie they set the input value n
'''For a given n this program converts it to binary and then returns the maximum number of consecutive 1s'''
import math
import os
import random
import re
import sys

def ConvertToBinary(n):  #The way to convert a base 10 to binary is to keep dividing e.g for 11
    binary_list = []     # 11/2 = 5r1, 5/2 = 2r1, 2/2 = 1r0, 1/2 = 0r1 --> we have 1011 (going from the
    while n>0:           # back!) ie 2^3 + 0 + 2^1 + 2^0 = 11
        binary_list.append(int(n%2)) 
        if n%2 == 0:  
            n = n/2   # so if we have an even number then we can just halve
        else:
            n = (n-1)/2  # if not e.g 15 then we want to write 7r1 so do 14/2 = 7 
    binary_list.reverse() #since we want the reverse
    
    longest = 0
    count = 0  # very important to have two counters, had to look this up online
    for number in binary_list:
        if number == 1:
            count = count + 1
        else:
            longest = max(longest, count)
            count = 0
    return max(longest, count) #Not just longest as if the list was [1,0,1,1,1] say the final for loop iteration will be in the count, the else statement wont be executed, so count will be 3 but longest still 1

   
    

if __name__ == '__main__':
    n = int(input())
    result = ConvertToBinary(n)
    print(result)