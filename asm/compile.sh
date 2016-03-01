#!/bin/bash
file=$1
fname=${file%.*}
nasm -f elf $1
ld -m elf_i386 -s -o "$fname" "$fname"".o"

