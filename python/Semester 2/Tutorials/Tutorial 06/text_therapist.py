import random

hedges = ("Please, tell me a little more.",
          "Many of my patients tell me the same thing.",
          "Please, carry on talking.",
          "What is your point?")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

# When removed, makes more sense
filter_words = ("because",
                "cause")

replacements = {"I": "you",     # First to second
                "me": "you",
                "my": "your",
                "we": "you",
                "us": "you",
                "mine": "yours",
                "I'm": "you're",
                "am": "are",
                "you": "I",     # Second to first
                "You": "I",
                "are": "am",
                "you're": "I'm",
                "your": "my",
                "yours": "mine"}

patient_history = []

text_replacements = {"you": "u",
                     "are": "r",
                     "be": "b",
                     "late": "l8",
                     "later": "l8r",
                     "once": "1ce",
                     "thanks": "ty",
                     "thank you": "ty",
                     "no problem": "np",
                     "easy": "ez",
                     "for": "4",
                     "to": "2",
                     "before": "b4",
                     "great": "gr8"}

vowel_dict = {"a": "",
              "e": "",
              "i": "",
              "o": "",
              "u": ""}


def removeVowels(word):
    if len(word) < 4:
        return word
    else:
        new_str = ""
        for char in word:
            new_str += vowel_dict.get(char, char)

        return new_str


def reply(sentence):
    """Builds and returns a reply to the sentence."""

    sentence = filter_out(sentence)

    probability = random.randint(1, 20)
    if probability <= 5:     # Still 1/4
        output = random.choice(hedges)
    elif 5 < probability < 8 and len(patient_history) > 5:  # Only after 5 replies
        output = "Earlier, you said that " + changePerson(patient_history.pop(0))
    else:
        output = random.choice(qualifiers) + changePerson(sentence) + "?"

    # After replying, add to history
    patient_history.append(sentence)

    return output


def filter_out(sentence):
    """Removes words in filter"""
    words = sentence.split()

    replyWords = []
    for word in words:
        if word not in filter_words:
            replyWords.append(word)

    return " ".join(replyWords)


def changetoText(sentence):
    """Replaces sentece with one containing text language"""
    words = sentence.split()

    replyWords = []
    for word in words:
        # This just lets you change words while keeping punctuation
        pre_punc = ""
        post_punc = ""
        if any(word[0] == punc for punc in ('.', '?', '!', ',')):
            pre_punc = word[0]
            word = word[1:]
        if any(word[-1] == punc for punc in ('.', '?', '!', ',')):
            post_punc = word[-1]
            word = word[:-1]

        replyWords.append(pre_punc + text_replacements.get(word, removeVowels(word)) + post_punc)

    return " ".join(replyWords)


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
    print(changetoText("Good morning, I hope that you are well today?"))
    print(changetoText("What can I do for you?"))

    # Main loop
    while True:
        sentence = raw_input("\n>> ")
        if sentence.upper() == "QUIT":
            print(changetoText("Have a nice day"))
            break
        print(changetoText(reply(sentence)))

main()
