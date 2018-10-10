'''Merge Sort. This will recursively divide an array to be sorted in half until it
reaches a base case of just one element which is already sorted. The sorted sub arrays
are then merged together in linear time! Total time complexity is nlogn.'''

import math

# Given an array with specified start index p, midpoint index q (rounded down) and end index r,
# with the sub arrays arr[p...q] and arr[q+1...r] already sorted merge them together so
# all of the elements are in order then, this function is theta(n) complexity. Crucial: if given e.g
# [1,2,3,4] and p=0 r=1 (so q=0) then we want low_half = [1] and high_half = [2], similarly
# if p=2 r=3 then we want [3] and [4] respectively. Initially I only had range(q+1) in first
# for loop and couldnt work out what was wrong for ages, as then low_half was [1,2,3] instead of [3]
# and there were some unecessary comparisons which increased k from 2 to 4 and then there was an IndexError
# when program tried to do arr[k]...
def Merge(arr, p, q, r):

    low_half = []
    high_half = []

    #First need to copy the array into two empty sub arrays, lowHalf and highHalf

    for i in range(p,q+1):
        low_half.append(arr[i])

    for i in range(q+1, r+1):
        high_half.append(arr[i])

    #print(low_half, high_half) #for testing and seeing how it works

    k = p
    i = 0
    j = 0

    # Repeatedly compare the lowest untaken element in lowHalf with the lowest untaken
    # element in highHalf and copy the lower of the two back into array

    while (i < len(low_half) and j < len(high_half)):

        if low_half[i] < high_half[j]:
            arr[k] = low_half[i]
            i = i+1

        else:
            arr[k] = high_half[j]
            j = j+1

        k = k+1

    # Once one of lowHalf and highHalf has been fully copied back into array,
    # copy the remaining elements from the other temporary array back into the array

    while i < len(low_half):
        arr[k] = low_half[i]
        i = i+1
        k = k+1

    while j < len(high_half):
        arr[k] = high_half[j]
        j = j+1
        k = k+1

#Given an array with start index p and end index r MergeSort() sorts the array recursively.
def MergeSort(arr, p, r):

    midpoint_index = math.floor((p + r)/2)

    #If index p is not < r then that means the array is of size 1 or zero and thus
    #is already sorted.
    if p < r:
        MergeSort(arr, p, midpoint_index)
        MergeSort(arr, midpoint_index + 1, r)
        Merge(arr, p, midpoint_index, r)


def Main():
    arr = [3, 1, 7, 6]
    arr2 = [3, -1, 7, 6, 0, 5, -10, 20]

    MergeSort(arr2,0,7)
    print("sorted array is: ", arr2)

    MergeSort(arr,0,3)
    print("sorted array is: ", arr)

Main()
