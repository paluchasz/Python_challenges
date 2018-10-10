
def CreateList(n):
    list_of_numbers = []
    for i in range(1, n+1):
        list_of_numbers.append(i)
    return list_of_numbers

def ConvertToBinary(n):  #The way to convert a base 10 to binary is to keep dividing e.g for 11
    binary_list = []     # 11/2 = 5r1, 5/2 = 2r1, 2/2 = 1r0, 1/2 = 0r1 --> we have 1011 (going from the
    while n>0:           # back!) ie 2^3 + 0 + 2^1 + 2^0 = 11
        binary_list.append(int(n%2))
        if n%2 == 0:
            n = n/2   # so if we have an even number then we can just halve
        else:
            n = (n-1)/2  # if not e.g 15 then we want to write 7r1 so do 14/2 = 7
    binary_list.reverse() #since we want the reverse
    return binary_list

def ConvertNumbersInListToBinary(n):
    list_of_numbers = CreateList(n)
    converted_list = []
    for num in list_of_numbers:
        x = ConvertToBinary(num)
        converted_list.append(x)
    return converted_list

if __name__ == '__main__':
    x = ConvertNumbersInListToBinary(5)
    print(x)
