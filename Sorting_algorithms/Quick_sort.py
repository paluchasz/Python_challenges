'''Quick Sort'''

# A function which swaps two elements in an array, arr[first] and arr[second]
def Swap(arr, first_index, second_index):
    temporary = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temporary

#The partition function should partition the subarray array[p..r] so that all elements
#in array[p..q-1] are less than or equal to array[q] (the pivot) and all elements
#in array[q+1..r] are greater than array[q], and it returns the index q of where the pivot ends up
#It is easiest to chose the pivot as the last element arr[r].

def Partition(arr,p,r):

    q = p

    for j in range(p, r): #we only want to go up until the pivot so not r+1 here
        if arr[j] <= arr[r]:
            Swap(arr, j, q)
            q += 1
        #print(arr) #use for testing and seeing how program works!

    Swap(arr, r, q)
    return q

# q is the index of the subarray with elements bigger than the pivot. Here is what the function
# does with [9,-7,5,0,12,2] p=0 and r=5: First it assigns q=0. It compares 9 with the pivot 2, since
# it is bigger we do not need to do anything. Now we look at -7 it is smaller than 2 so we swap -7
# with 9 to obtain [-7,9,5,0,12,2] and increment q to 1 since now the sublist with biggere elements
#starts at q=1. Then compare 5 > 2 and do nothing. Then 0<2 and so we swap 0 with 9 giving
#[-7,0,5,9,12,2] and increment q to 3 (and indeed 5 is now the first element of the bigger subarray)
#12>2 so nothing happens, finally we leave the lopp and swap 2 with 5 to get [-7,0,2,9,12,5], so
#it correctly placed all smaller elements to the left of the pivot =2 and all bigger elements to the right

# Finally we have a function which recurseviley partitions the array. As in mergesort once p is not less than r
# we have a list of just one or zero elements which is already sorted and we don't have to do anything.
def QuickSort(arr, p, r):

    if p < r:
        pivot = Partition(arr, p, r)
        QuickSort(arr, p, pivot-1)
        QuickSort(arr, pivot+1, r) #note we are leaving the arr[pivot] intact!


def Main():
    arr = [9,-7,5,0,12,2]
    Partition(arr,0,len(arr)-1)
    print(arr)
    arr2 = [8,9,-3,-5,0,1,-1,6]
    Partition(arr2,0,7)
    print(arr2)
    arr3 = [8,9,-3,-5,0,1,-1,6]
    QuickSort(arr3, 0, len(arr3)-1)
    print(arr3)

Main()
