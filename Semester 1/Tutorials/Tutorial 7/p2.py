#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "p2.py", "4/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")

sentence = input("Enter a sentence: ")

split_sentence = sentence.split()

caps = [word.title() for word in split_sentence]
uppercase = [word.upper() for word in split_sentence]

print(split_sentence)
print(caps)
print(uppercase)