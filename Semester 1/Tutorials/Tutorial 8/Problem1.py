#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
    "Problem1.py", "11/05/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


def write_chunk(filepath, lines):
    with open(filepath, "w") as f:
        f.writelines(lines)

file = input("Save to what file: ")
write_lines = []

while True:
    user_input = input(">")

    if user_input == '.':
        break
    else:
        write_lines.append(user_input + "\n")

write_chunk(file, write_lines)