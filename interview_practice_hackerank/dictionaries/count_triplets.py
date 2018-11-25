'''You are given an array and you need to find number of tripets of indices
such that the elements at those indices are in geometric progression
for a given common ratio r and i<j<k'''

# Idea is to keep track of a middle element arr[i] which is divisible by r and then
# finding out how many elements to the left have value arr[i]/r and how many to the
# right have value arr[i]*r. Use two dictionaries, one for elements to the left, and
# one with elements to the right. So for the left dicitionary I will keep adding to it
# as i go through the middle elements and for the right dictionary i will have to start
# of with a full dict and remove from it as I loop through the arr for middle element.

def countTriplets(arr, r):
    elements_to_left = {arr[0]:1}
    elements_to_right = {}
    triplets = 0

    # So I start at 2nd index of arr when creating elements_to_right which is weird
    # but that's because then in the next loop I delete it before I even look at the count
    # Reason for this is that deleting a key for position i+1 was running into problems
    # if that wasn't in the dictionary.
    for i in range(1, len(arr)):
        if arr[i] == 1 or arr[i] % r == 0:
            elements_to_right[arr[i]] = elements_to_right.get(arr[i], 0) + 1
            # 2nd argument in get() ensures that if no value exists for the
            # key arr[i] it will return 0

    # let's say triplets are of the form (first, middle, last)
    for i in range(1, len(arr) - 1):
        # check for possible middle element:
        middle = arr[i]

        if middle % r == 0:
            first = middle/r
            last = middle*r

            # Decrease frequency of key/remove key in right dictionary
            if elements_to_right[middle] == 1:
                elements_to_right.pop(middle)
            else:
                elements_to_right[middle] -= 1

            # check how many first elements there are in elements_to_left
            count_of_first = elements_to_left.get(first, 0)
            # check how many last elements there are in elements_to_right
            count_of_last = elements_to_right.get(last, 0)

            # if the current middle = 3 say and there are 2 1s to the left and 2 9s
            # to the right then clearly number of possible triplets for this middle
            # element is 2x2=4!
            triplets += count_of_first * count_of_last

        # add to left dicitionary as we loop
        elements_to_left[middle] = elements_to_left.get(middle, 0) + 1

    return triplets

def openFile(path):
    F = open(path, 'r')
    x = [int(y) for y in F.read().split(' ')]
    return x


if __name__ == '__main__':
    # arr = [1, 3, 5, 9, 9, 12, 15, 27, 1]
    # arr2 = [1, 1, 1, 1, 1, 1, 1, 1]
    # arr3 = [1, 74, 8, 16, 88]
    # result = countTriplets(arr, 3)
    # print(result)
    # result2 = countTriplets(arr2, 1)
    # print(result2)
    # result3 = countTriplets(arr3, 2)
    # print(result3)
    x = openFile("test_case.txt")
    result = countTriplets(x, 3)
    print(result)
