# clippy finds all words that can be formed without rearranging the alphabet

import sys

def find_words(dictionary):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    words = []
    for i in range(len(alphabet)):
        for candidate in words_around(i, alphabet):
            if candidate in dictionary:
                words.append(candidate)

    return set(words)

def words_around(center, sequence):
    ''' words_around(2,abcd) => [ab, b, bc, bcd, abc, abcd]'''

    for i in reversed(range(center)):
        yield sequence[i:center+1]

    for i in range(center+1, len(sequence)+1):
        yield sequence[center:i]

    for i in range(1, max(len(sequence)-center, center+1)+1):
        yield sequence[max(center-i,0):center+i]

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        print("Usage: $python clippy.py dictionary.txt")
        exit()

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        dictionary = dict()
        for word in file:
            dictionary[word.rstrip()] = 1

        words_found = find_words(dictionary)
        print("Found {} words".format(len(words_found)))
        for w in words_found:
            print w

if __name__ == '__main__':
    main()

