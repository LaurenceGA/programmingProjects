#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem2.py", "11/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def copy_file_contents(copy_file, new_file):
    with open(copy_file, 'r') as cf:
        text = cf.read()

    with open(new_file, 'w') as wf:
        wf.write(text)

copy_file_contents(input("File to copy: "), input("File to write to: "))