#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem3.py", "11/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def copy_file_contents(copy_file, new_file):
    try:
        f = open(copy_file, 'r')
        lines = f.readlines()
        f.close()
    except IOError as e:
        print(e)
        return

    try:
        lines_omit_begin = int(input("Omit how many lines from the start: "))
        lines_omit_end = int(input("Omit how many lines from the end: "))
    except ValueError as e:
        print(e)

    if len(lines) > 0 and len(lines) >= lines_omit_begin + lines_omit_end:
        with open(new_file, 'w') as wf:
            wf.writelines(lines[lines_omit_begin:len(lines)-lines_omit_end])
    else:
        print("Incorrect number of lines")

copy_file_contents(input("File to copy: "), input("File to write to: "))