# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:53:40 2019

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t)
the Hamming distance between two strings of equal length is the number of
positions at which the corresponding symbols are different.
.
@author: Jess
"""

file = open("rosalind_hamm.txt", "r")
listoflists = []
for seq in (file.read().splitlines()):
    listofbases = []
    for base in seq:
        listofbases.append(base)
    listoflists.append(listofbases)
seq1 = listoflists[0]
seq2 = listoflists[1]

mismatch = 0
for i in range(0, len(seq1)):
    if seq1[i] != seq2[i]:
        mismatch += 1
print(mismatch)

file.close()
