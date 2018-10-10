'''This program will be a Bubble sort algorithm. Idea of Bubble sort is to
go through the list and compare numbers next to each other and swap if
necessary. Keeping a count of swaps in each pass the program terminates when there
have been 0 swaps indicating the list is ordered.'''

def BubbleSort(arr):
    swaps = 0
    current_swaps = True

    while current_swaps:

        current_swaps = False
        for i in range(len(arr)-1):

            if arr[i] > arr[i+1]:
                temporary = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temporary
                current_swaps = True
                swaps += 1
    print("number of swaps:", swaps)
    return arr

def main():
    arr = [2,1,5,3,4]
    arr2 = [1,-1,0,3]
    result = BubbleSort(arr)
    print(result)
    result2 = BubbleSort(arr2)
    print(result2)

main()
