'''Given two string this program finds if they share a common substring'''

def twoStrings(s1, s2):
    # First create dictionary for characters in string s1
    s1_dict = {}

    for char in s1:
        if char not in s1_dict:
            s1_dict[char] = 1
        else:
            s1_dict[char] += 1

    # Now only need to go through characters in s1 and if any of them is in s1
    # then that means they share a common substring so we return "YES" and we stop
    for char in s2:
        if char in s1_dict:
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
