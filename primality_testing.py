#Primality tests. To check if n is prime we need to check that it doesn't divide integers less than n.
#This would be a linear O(n) time complexity. However, we can do better by noting that sqrt(n)*sqrt(n) = n.
#Because of this if we look at integer higher than sqrt(n) then if it divides n it's other factor will have to be
#an integer smaller than sqrt(n) but we would have already considered this integer. Hence this algorithm is O(n^1/2) 
import math

def isPrimeV1(n):
    if n == 1:
        return "Not prime"

    square_root = math.sqrt(n)
    round_square_root = int(round(square_root))

    for i in range(2, round_square_root+1):
        if n % i == 0:
            #print(n, i) a little comment to check what's going on
            return "Not prime"

    return "Prime"

result = isPrimeV1(33)
print(result)
