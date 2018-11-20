'''Given an array of words in a note and an array of words in a magazine we want to
see if using the words from the magazine we can reconstruct the note. The words
are case sensitive and we can only use each word once. So if the note has two words
'two' then we need at least two 'two' in the magazine'''

def checkMagazine(magazine, note):

    magazine_dict = {}
    note_dict = {}

    # for each of the arrays create a dictionary so that we
    # know the frequency of each word
    for word in note:
        if word not in note_dict:
            note_dict[word] = 1
        else:
            note_dict[word] += 1

    for word in magazine:
        if word not in magazine_dict:
            magazine_dict[word] = 1
        else:
            magazine_dict[word] += 1

    # now we want to go through note_dict and check if there is
    # a corresponding word in magazine_dict with at least the same frequency

    for key in note_dict:

        if key in magazine_dict:
            if note_dict.get(key) <= magazine_dict.get(key):
                # get() returns value for given key
                pass
            else:
                return "No"

        else:
            return "No"

    return "Yes"

if __name__ == '__main__':
    mn = input().split()
    # two numbers specyfing how many words in note and magazine

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()
    # magazine is an array of strings now

    note = input().rstrip().split()

    result = checkMagazine(magazine, note)
    print(result)
