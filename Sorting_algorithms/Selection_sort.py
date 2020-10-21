'''Selection sort algorithm. Find the smallest element in the list and put it
in first place. Then find the second smallest and put it in second place etc'''

def SelectionSort(arr):

    index_of_smallest_element = 0

    #Have len(arr)-1 since only need to go up to previous to last index since if this one
    #is swapped with the last one then the list is sorted
    for i in range(len(arr)-1):

        smallest_element = arr[i]
        #Need to initialise the smallest element variable with each iteration

        #Idea is for each index of array only look at the smaller array next to it and Find
        #the smallest element in it and swap it with the element at current index. Hence the i+1.
        for j in range(i+1, len(arr)):
            if arr[j] < smallest_element:
                smallest_element = arr[j]
                index_of_smallest_element = j

        #The next 3 lines swap the two elements
        temporary = arr[i]
        arr[i] = smallest_element
        arr[index_of_smallest_element] = temporary
        #print(arr) if I want to see the array after each swap

    return arr


def main():
    arr = [-10,2,2,2,1,8,-1,-5]
    result = SelectionSort(arr)
    print(result)

main()
