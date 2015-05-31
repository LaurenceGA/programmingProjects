#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Question 1.py", "7/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

from random import choice, randint   # No point importing the entire module
import sys

cols = {
    'white':    "37",
    'yellow':   "33",
    'green':    "32",
    'blue':     "34",
    'red':      "31",
    'black':    "30"
}


def colour(string, col):
    """Adds colour character codes and returns the given string coloured"""
    if hasattr(sys.stdout, "isatty"):
        return "\033[1;{}m".format(col) + string + "\033[0;0m"
    else:
        return string


def read_file(filepath):
    """Return contents of a file as a list. Removes \n characters"""
    with open(filepath) as f:
        return f.read().splitlines()


def load_words(file_list):
    all_words = {}
    for file in file_list:
        try:
            # Get list of words from file and add with filename as key
            all_words[file] = read_file(file + ".txt")
        except IOError:
            print(colour("Error! Could not find file {}!".format(file), cols['red']))

    if all_words:   # If at least some words were loaded
        print(colour("Words loaded.", cols['green']))

    return all_words


def capitalize_string(string):
    """split a string into words, capitalize where appropriate (!?.)"""
    string = string.capitalize().split(" ")
    for i, word in enumerate(string):
        if i < len(string)-1:
            if '!' in word or '?' in word or '.' in word:
                string[i+1] = string[i+1].capitalize()

    return " ".join(string)


def test_load(words):
    # Display first word of each list
    if words:
        for typ, word_list in words.items():
            print(typ + colour(":", cols['yellow']), word_list[0])
    else:
        print(colour("Error! Words have not been loaded!", cols['red']))


def add_favourite(faves, sent):
    if sent:
        if sent not in faves:
            faves.append(sent)
            print("{}\n    ".format(sent) + colour("Was added to favourites!", cols['green']))
        else:
            print(colour("Already a favourite!", cols['red']))
    else:
        print(colour("Nothing to add.", cols['red']))


def display_favourites(faves):
    for fave in faves:
        print('- ' + fave)


def terminate():
    print(colour("Goodbye.", cols['blue']))
    raise SystemExit    # Clean way to exit program


def easy_sentence(words, noun=""):
    if not words:
        print(colour("Error! Words have not been loaded!", cols['red']))
        return None, None

    if not noun:    # Pick a noun if none given
        noun = choice(words["Nouns"])

    intrans_verb = choice(words["IntransitiveVerbs"])

    final_sentence = capitalize_string("{} {}.".format(noun, intrans_verb))

    return final_sentence, noun


def noun_phrase(words, noun=""):
    # <Noun-Phrase> ::= <Noun-marker> [ <Adjective> ] <Noun>
    if not words:
        print(colour("Error! Words have not been loaded!", cols['red']))
        return None, None

    noun_marker = choice(words["NounMarkers"]) + " "                # Pick a noun marker
    adjective = choice([choice(words["Adjectives"]) + " ", ""])     # Pick an adjective maybe

    if not noun:                                                    # Pick a noun if none given
        noun = choice(words["Nouns"])

    final_phrase = "{}{}{}".format(noun_marker, adjective, noun)

    return final_phrase, noun


def verb_phrase(words):
    # <Verb-Phrase> ::= <Intransitive-verb> | <Transitive-verb> <Noun-phrase>
    if not words:
        print(colour("Error! Words have not been loaded!", cols['red']))
        return None, None

    if choice([True, False]):       # 50/50
        final_phrase = choice(words["IntransitiveVerbs"])   # Grab intransitive verb
    else:
        verb = choice(words["TransitiveVerbs"]) + " "       # Grab transitive verb
        n_phrase, _ = noun_phrase(words)                    # Grab noun_phrase, discard noun

        final_phrase = "{}{}".format(verb, n_phrase)

    return final_phrase


def sentence(words, noun=""):
    if not words:
        print(colour("Error! Words have not been loaded!", cols['red']))
        return None, None

    # <Sentence>::= [<Lead-in>] <Noun-Phrase> [<Adverb>] <Verb-Phrase>.
    leadin = choice([choice(words["Leadin"]) + " ", ""])        # Grab a leadin maybe
    n_phrase, noun = noun_phrase(words, noun)                   # Grab a noun phrase
    n_phrase += " "

    adverb = choice([choice(words["Adverbs"]) + " ", ""])       # Grab an adverb maybe
    v_phrase = verb_phrase(words)                               # Grab a verb phrase

    final_sentence = capitalize_string("{}{}{}{}.".format(leadin, n_phrase, adverb, v_phrase))

    return final_sentence, noun


def paragraph(words):
    if not words:
        print(colour("Error! Words have not been loaded!", cols['red']))
        return

    r_noun = choice(words["Nouns"])

    sentence_number = randint(3, 5)     # From random module

    para = []

    for part in range(sentence_number):
        if choice((True, False)):   # Double sentence?
            sent1 = choice((sentence(words, r_noun), easy_sentence(words, r_noun)))[0][:-1]
            sent1 += " "
            conj = choice(words["Conjunctions"]) + " "
            sent2 = choice((sentence(words, r_noun), easy_sentence(words, r_noun)))[0]

            para.append(capitalize_string("{}{}{}".format(sent1, conj, sent2)))
        else:
            sent = choice((sentence(words, r_noun), easy_sentence(words, r_noun)))[0]

            para.append(capitalize_string(sent))

    print("\n".join(para))      # Otherwise prints on one line


def get_command(r_noun):
    # The menu
    r_cycle = colour("on", cols['green']) if r_noun else colour("off", cols['red'])
    # Use list comprehension to colour each command string more easily
    commands = [colour(com, cols['blue']) for com in ['L', 'T', 'E', 'S', 'P', 'N', 'F', 'A', 'C', 'Q']]

    print("[{}]: Load words, [{}]: Test words\n"
          "[{}]: Easy sentence, [{}]: Full sentence, [{}]: Paragraph\n"
          "[{}]: Toggle noun recycling (Currently: {r_cycle})\n"
          "[{}]: Display favourites, [{}]: Add to favourites, [{}]: Clear favourites\n"
          "[{}]: Quit".format(*commands, r_cycle=r_cycle))
    return input(colour("Enter a command: ", cols['blue']))

files = (
    "Adjectives",
    "Adverbs",
    "Conjunctions",
    "IntransitiveVerbs",
    "Leadin",
    "NounMarkers",
    "Nouns",
    "TransitiveVerbs"
)

word_dict = {}
previous_sentence = ""
favourites = []

recycle_noun = False
remembered_noun = ""

while True:
    cmd = get_command(recycle_noun).lower()
    print(colour("-----" * 15, cols['yellow']))

    if cmd == 'l':
        if not word_dict:
            word_dict = load_words(files)
        else:
            print(colour("Words are already loaded.", cols['red']))

    elif cmd == 't':
        test_load(word_dict)

    elif cmd == 'e':
        cycling_noun = remembered_noun if recycle_noun else ""
        previous_sentence, remembered_noun = easy_sentence(word_dict, cycling_noun)

        if previous_sentence:
            print(previous_sentence)

    elif cmd == 's':
        cycling_noun = remembered_noun if recycle_noun else ""
        previous_sentence, remembered_noun = sentence(word_dict, cycling_noun)

        if previous_sentence:
            print(previous_sentence)

    elif cmd == 'p':
        paragraph(word_dict)
        previous_sentence = ""

    elif cmd == 'n':
        recycle_noun = not recycle_noun
        recycle = colour("on", cols['green']) if recycle_noun else colour("off", cols['red'])
        print("Noun recycling now {}".format(recycle))

    elif cmd == 'a':
        add_favourite(favourites, previous_sentence)

    elif cmd == 'f':
        if favourites:
            display_favourites(favourites)
        else:
            print(colour("Favourites is empty.", cols['red']))

    elif cmd == 'c':
        if favourites:
            if input("Are you sure? ").lower() in ['yes', 'y', 'yep']:
                favourites.clear()
                print(colour("\nFavourites cleared.", cols['green']))
            else:
                print(colour("\nFavourites not cleared.", cols['red']))
        else:
            print(colour("Favourites already empty.", cols['red']))

    elif cmd == 'q':
        terminate()
    else:
        print(colour("Please enter an appropriate command.", cols['red']))

    print(colour("-----" * 15, cols['yellow']))