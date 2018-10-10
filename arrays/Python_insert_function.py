'''Code for Pthon insert function'''
def Insert(arr, right_index, value):

    arr.append(value)

    for i in range(len(arr)-2, right_index -1, -1):
        arr[i+1] = arr[i]

    arr[right_index] = value
