def array_manipulation(n, queries):
    """Idea is to keep an array which stores how much one element is bigger than the previous element.
    E.g. [3, 0, 0, -3, 0] corresponds to [3, 3, 3, 0, 0] as the 2nd element is 3 + 0, 3rd element is 2nd element + 0 = 3
    and 4th element is 3rd element -3 = 0"""
    array = [0 for _ in range(n)]
    for query in queries:
        start_idx = query[0] - 1
        one_after_end_idx = query[1]
        array[start_idx] += query[2]
        if one_after_end_idx < n:  # avoids index error
            array[one_after_end_idx] -= query[2]

    current_max = 0
    current_value = 0
    for num in array:
        current_value += num
        if current_value > current_max:
            current_max = current_value

    return current_max


if __name__ == '__main__':
    with open('/home/paluchasz/Dropbox/programming/Python_challenges/interview_practice_hackerank/Arrays/big_test_case.csv', 'r') as file:
        data = file.readlines()
        for i, line in enumerate(data):
            data[i] = [int(d) for d in line.replace('\n', '').split(' ')]
    n = data[0][0]
    queries = data[1:]
    max_value = array_manipulation(n, queries)
    print(max_value)

    # simple

    queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    max_value = array_manipulation(10, queries)
    print(max_value)

    print(array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))
