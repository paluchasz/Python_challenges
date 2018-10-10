''' This program reverses a given sentence'''

def printInReverse(sentence):
    list_of_words = list( map(str, sentence.split()) )
    reverse_string = ""
    for i in range( len(list_of_words) - 1, -1, -1):
        reverse_string = reverse_string + list_of_words[i] + " "
    return reverse_string

if __name__ == '__main__':
    print("Please write a sentence!")
    sentence = input() #Use this for python3 and raw_input for python2 (ie python in terminal)
    print("The reverse sentence is:")
    reverse_string = printInReverse(sentence)
    print(reverse_string)
