'''Find minimum number of swaps in an array of n elements. The idea is that the min
number of swaps is the sum from 1 to number of cycles of (cycle_size - 1). E.g
for [2,4,5,1,3] we have 2 cycles one between 5 and 3 which is size 2 and requires 1 swap
and one between 2 4 and 1 which is of size 3 and requires 2 swaps. So total swaps of 3.

Reference: https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/ '''


def MinSwaps(arr):

    n = len(arr) #e.g for [2,4,5,1,3]

    arr_position = list(enumerate(arr)) #[(0, 2), (1, 4), (2, 5), (3, 1), (4, 3)]

    arr_position.sort(key = lambda element: element[1]) #[(3, 1), (0, 2), (4, 3), (1, 4), (2, 5)]
    #Lambda is a function with no name, e.g double = lambda x: x*2 then double(5) = 10, lambda takes
    # x as the argument and returns x*2

    #Create an empty list of False.
    visited = []
    for k in range(len(arr)):
        visited.append(False)

    ans = 0

    for i in range(len(arr)):

        if visited[i] or arr_position[i][0] == i:
            continue
        #continue makes the program ignore the rest of the loop in this iteration
        #which is exactly what we want if it element has already been visited or is
        #in the correct place. If the arr is already sorted then 2nd assertion is always true!

        cycle_size = 0
        j = i
        while not visited[j]: #ie when visited element is False so not visited yet
            visited[j] = True

            j = arr_position[j][0] #in our example j is 0 then 3 then 1 and visited[1] is already
                                   #True by then so we stop while loop
            cycle_size += 1

        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans


#Python enumertate() e.g:
#arr = [2,4,5,1,3]
#enumerate_arr = enumerate(arr)
#print(enumerate_arr) # prints <enumerate object at 0x7ff5eb6ac558>
#print(list(enumerate_arr)) # prints [(0, 2), (1, 4), (2, 5), (3, 1), (4, 3)]
#enumerate_arr[i][j] gives the jth element of ith tuple, so enumerate_arr[1][1] = 4
#and enumerate_arr[2][0] = 2 for example

#e.g of Python Sort() function:
#arr2 = [(0, 2), (1, 4), (2, 5), (3, 1), (4, 3)]
#def takeSecond(elem):
#    return elem[1]
#arr2.sort(key = takeSecond)
#print(arr2) would give [(3, 1), (0, 2), (4, 3), (1, 4), (2, 5)]


def Main():
    arr = [2,4,5,1,3]
    result = MinSwaps(arr)
    print(result)

Main()
