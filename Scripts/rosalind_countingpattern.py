# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:14:17 2020

@author: Jess
Compute the Number of Times a Pattern Appears in a Text
Given: {DNA strings}} Text and Pattern.

Return: Count(Text, Pattern).
"""
seq = ''
pattern = ''
with open("rosalind_countingpattern.txt", "r") as file:
    info = file.readlines()
    seq = info[0].strip()
    pattern = info[1].strip()
# print(seq)
# print(pattern)

count = 0
for i in range(0, len(seq)):
    if seq[i:i+len(pattern)] == pattern:
        count = count + 1
print(count)
