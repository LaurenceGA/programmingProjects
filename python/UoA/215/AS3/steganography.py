#!/usr/bin/env python
from sys import stdout

__author__ = "Laurence"
authorship_string = "{} created on {} by {}\n{}\n".format(
    "steganography.py", "9/03/2016", __author__, "-----" * 15) \
    if __name__ == '__main__' else ""
stdout.write(authorship_string)

import cImage


base_image = cImage.FileImage('Steganography-larm315.png')


class ImageReader(object):
    def __init__(self, image):
        self.image = image
        self.width, self.height = base_image.getWidth(), base_image.getHeight()

        self.lsbs = []

        for row in range(self.height):
            for col in range(self.width):
                px = self.image.getPixel(col, row)

                # self.lsbs.append(px.getRed() & 1)
                # self.lsbs.append(px.getGreen() & 1)
                # self.lsbs.append(px.getBlue() & 1)
                self.lsbs.extend([px.getRed() & 1, px.getGreen() & 1, px.getBlue() & 1])

        self.read_pos = 0
        print("read image...\n")

    def get_next_bit(self):
        b = self.lsbs[self.read_pos]
        # print("{}: {}".format(self.read_pos, b))
        self.read_pos += 1
        return b

    def read_text_length(self):
        # Read the first 32 LSBs
        length = []
        # length = self.get_next_bit()
        for i in range(32):
            length.insert(0, str(self.get_next_bit()))
            # length <<= 1
            # length |= self.get_next_bit()

        length = int("".join(length), 2)

        # Reverse
        # length = int(bin(length)[:1:-1], 2)
        # self.get_next_bit()

        return length

    def get_next_byte(self):
        char = []
        for i in range(8):
            # char <<= 1
            # char |= self.get_next_bit()
            char.insert(0, str(self.get_next_bit()))

        char = int("".join(char), 2)
        # Reverse
        # char = int(bin(char)[:1:-1], 2)
        # self.get_next_bit()

        return char


reader = ImageReader(base_image)

text_length = reader.read_text_length()
print("Text length: {}".format(text_length))

text_bytes = []
for b in range(text_length):
    text_bytes.append(reader.get_next_byte())

for b in text_bytes:
    print(chr(b), end="")
print()


