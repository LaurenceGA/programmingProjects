#!/usr/bin/env python
from sys import stdout

__author__ = 'Laurence Armstrong'
authorship_string = "{} created on {} by {} ({})\n{}\n".format(
        "CrackManyTimePad.py", "7/03/16", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

encrypted_text = """\
1401E0A64DE019290B2B8A4C227D3ED411E9B3ADB1AB313973DE
0116E4A64DFA193E4E64824E7B343E8413E3B9B7F2AA3A2A7ACF
1301E2F45CE60F6C4A3686006C713B910EACA7B6BBB43E2C7ADE
170CF8A658E0196C582B8E452272219B0BE9A5B7F2A0332D7ACF
1401E0E551F70E3F0B2B8554677A6D810FE9F7B7A6AB3C336CDE
0A05EFE34DB21F204E258D456634399C19ACBCADA6A1373D71DE
1401EDE34FFB0F25442AC3446D713ED41EFEB8A5B6A13E2B6BDE\
"""

sentences = encrypted_text.split('\n')

b_sentences = []
for n in range(len(sentences)):
    b_sentences.append([])

cnt = 0
for s in sentences:
    # print(s)
    for i in range(0, len(s), 2):
        b_sentences[cnt].append(int(s[i:i+2], 16))
    for b in b_sentences[cnt]:
        print("{:2X}".format(b), end=", ")
    print("\t{}".format(cnt))
    cnt += 1

sentences = b_sentences

key = [0x00] * len(sentences[0])

key[0] = ord('T') ^ 0x14
key[1] = ord('e') ^ 0x01
key[2] = ord('y') ^ 0xF8
key[3] = ord(' ') ^ 0xA6
key[4] = ord('e') ^ 0x5C
key[5] = ord('t') ^ 0xE6
key[6] = ord('s') ^ 0x0F
key[7] = ord('i') ^ 0x25
key[8] = ord('o') ^ 0x44
key[9] = ord('n') ^ 0x2A
key[10] = ord('e') ^ 0x86
key[11] = ord('e') ^ 0x45
key[12] = ord(' ') ^ 0x22
key[13] = ord(' ') ^ 0x34
key[14] = ord(' ') ^ 0x6D
key[15] = ord(' ') ^ 0xD4
key[16] = ord('r') ^ 0x0E
key[17] = ord(' ') ^ 0xAC
key[18] = ord('r') ^ 0xA5
key[19] = ord('i') ^ 0xAD
key[20] = ord(' ') ^ 0xF2
key[21] = ord('v') ^ 0xB4
key[22] = ord('a') ^ 0x3E
key[23] = ord('t') ^ 0x2C
key[24] = ord('e') ^ 0x7A
key[25] = ord('.') ^ 0xDE

# print(key)


def print_plain(txt, key):
    j=0
    for sentence in txt:
        i = 0
        for byt in sentence:
            if key[i] == 0x00:
                # print(hex(byt)[2:], end='')
                print("--", end='')
            else:
                print(chr(byt ^ key[i]), end='')
            i += 1
        print("\t{}".format(j))
        j += 1

print()
for i in range(len(sentences[0])):
    print("{:2}, ".format(i), end='')

print('\n')

def xor_two(s1, s2):
    result = []
    for i in range(len(s1)):
        result.append(s1[i] ^ s2[i])
    return result

def print_bytes(byts):
    for b in byts:
        print(chr(b), end='')
    print()

print_plain(sentences, key)

# print_bytes(xor_two(sentences[0], sentences[1]))
