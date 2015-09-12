import random

hedges = ( "Please, tell me a little more.",
           "Many of my patients tell me the same thing.",
           "Please, carry on talking.",
           "What is your point?")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {"I": "you",
                "me": "you",
                "my": "your",
                "we": "you",
                "us": "you",
                "mine": "yours",
                "am": "are"}

text_replacements = {"you": "u",
                     "are": "r",
                     "be": "b"}

vowels = ('a', 'e', 'i', 'o', 'u')
vowel_dict = {"a": "",
              "e": "",
              "i": "",
              "o": "",
              "u": ""}


def removeVowels(word):
    if len(word) <= 4:
        return word
    else:
        word_list = list(word)
        for i, char in enumerate(word_list):
            if char in vowels:
                del word_list[i]

        return "".join(word_list)

def removeVowels2(word):
    if len(word) <= 4:
        return word
    else:
        new_str = ""
        for char in word:
            new_str += vowel_dict.get(char, char)


def reply(sentence):
    """Builds and returns a reply to the sentence."""
    
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence) + "?"


def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns."""
    words = sentence.split()

    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))

    return " ".join(replyWords)


def main():
    """Handles the interaction between patient and doctor."""
    # Introduction
    print("Good morning, I hope that you are well today?")
    print("What can I do for you?")

    # Main loop
    while True:
        sentence = raw_input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day")
            break
        print(reply(sentence))

main()
