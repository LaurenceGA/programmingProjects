#!/usr/bin/env python
# 159.171 Assignment 2A
# Laurence Armstrong, 15062061
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
                    "158171_A2A.py", "31/03/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def readFile(filepath):
    # Read text from a file and return it as a string
    # You don't need to change this function
    file = open(filepath, "rt")     # open the file
    outText = file.read()           # read the file
    file.close()                    # close the file
    return outText                  # return it as a string


def stripChars(text):
    # Part 1
    # Strip all chars in sChars from text
    # Output the edited string as text at the end

    sChars = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

    for chr in sChars:
        text = text.replace(chr, " ")

    return text


def displayStats(inText):
    # Part 2
    # Display the top 10 most frequently used words from inText
    # Frequency count is case insensitive

    wordList = inText.lower().split()       # Convert to lowercase and split text into a big list of words
    wordFrequencies = {}                    # Make a dictionary to hold frequency for each word

    for word in wordList:
        wordFrequencies[word] = wordFrequencies.get(word, 0) + 1    # Give each word a frequency

    """
    The following line creates a frequency list by:
    -getting list of tuples
    -create anonymous function to sort by the tuples' second indexes (frequency)
    -reverse to put in descending order
    """
    sortedWordFreq = sorted(wordFrequencies.items(), key=lambda x: x[1], reverse=True)

    print("Top 10 most frequently used words:")
    for wordFreq in range(10):
        # Check if the following entry has same frequency
        additionalStr = ""

        if sortedWordFreq[wordFreq+1]:
            if sortedWordFreq[wordFreq+1][1] == sortedWordFreq[wordFreq][1]:
                additionalStr = ", the same as #{:}, \"{}\"".format(wordFreq + 2, sortedWordFreq[wordFreq+1][0])

        # Display word, its position and frequency
        print('#{:<3} {:<10} was used {:2} times{}'.format(
            wordFreq + 1, '"'+sortedWordFreq[wordFreq][0]+'"', sortedWordFreq[wordFreq][1], additionalStr))


def decipherText(inText):
    # Bonus Question
    # Decrypt the text in the file 'pythonwiki_cipher.txt'
    # Display your result

    outText = ""
    orgKey      = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    cipherKey   = 'Cn9mcLX6U`v41(g\D8z~a<>:k"!S3GMf7d$%u{T?I#Osot|ry5]FN@2;BKe*[}Ww0.A,+-hPqHRZjVY=Jx)_lQb^/\'pE&i'

    for char in inText:
        # Will throw an error if the character isn't in the cipher key.
        try:
            outText += orgKey[cipherKey.index(char)]
        except ValueError:
            outText += char     # If it isn't in the key (e.g '\n', ' '), just keep the character the same

    print(outText)

if __name__ == '__main__':
    text = readFile('pythonwiki.txt')
    # print(text)

    # Part 1
    editedText = stripChars(text)
    print(editedText)

    # Part 2
    # displayStats(editedText)

    # Bonus Question
    cipherText = readFile('pythonwiki_cipher.txt')
    # decipherText(cipherText)
