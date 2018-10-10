#Primality tests
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
