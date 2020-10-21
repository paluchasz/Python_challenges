'''Insertion Sort: The idea of this is to keep an ordered list to the left and then
inspect values to the right one by one and insert them in the correct position in the
ordered list on the left. This is done by looping from the right and moving the elements to
the right to make space for the new element.'''


def insertionSort(arr):

#start at i=1 and our a[0] is a sorted sublist since it is just one element
    for i in range(1, len(arr)):
        temporary = arr[i]
        print(arr) #to see how it works

        while i>0 and arr[i-1] > temporary: #this was the crucial step to have i>0 too to avoid IndexError
            arr[i] = arr[i-1]               #and not some try/except statements..
            i -= 1

        arr[i] = temporary

    return arr

def main():
    arr = [4,2,8,3,1,5,6]
    result = insertionSort(arr)
    print(result)
    arr2 = [-1,8,-5,0,3,4,1,2]
    result2 = insertionSort(arr2)
    print(result2)

main()
