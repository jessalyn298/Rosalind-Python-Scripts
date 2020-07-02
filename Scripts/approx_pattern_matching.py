# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:18:37 2020

@author: Jess

Approximate Pattern Matching Problem

Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.
Return: All starting positions where Pattern appears as a substring of
Text with at most d mismatches.
"""
info = []  # get info from file
with open("rosalind_patternmatching.txt", "r") as file:
    info = file.readlines()
pattern = info[0].strip()  # assign info to variables from list of lines
sequence = info[1].strip()
maxmismatch = int(info[2].strip())
# print(info, pattern, sequence, maxmismatch)

list_of_substrings = []  # make a list of substrings of pattern length
for i in range(0, len(sequence)):
    mismatch = 0
    subseq = sequence[i:i+len(pattern)]
    if len(subseq) == len(pattern):
        list_of_substrings.append(subseq)

indeces = []  # loop over substrings, and for each, check mismatches.
for index, substring in enumerate(list_of_substrings):
    mismatch = 0
    for j in range(0, len(pattern)):
        if substring[j] != pattern[j]:
            mismatch += 1
    if mismatch <= maxmismatch:
        indeces.append(index)

print(" ".join(map(str, indeces)))
