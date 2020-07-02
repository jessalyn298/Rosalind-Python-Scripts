# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:51:11 2019

Reverse complement of a sequence from a file with a string. 

@author: Jess
"""

file = open("rosalind_revc.txt", "r")
t = file.readline()
revcomp = ""
# print(t)
for i in t:
    if i == "A":
        i = "T"
    elif i == "T":
        i = "A"
    elif i == "G":
        i = "C"
    elif i == "C":
        i = "G"
    revcomp = revcomp+i
print(revcomp[::-1])

file.close()
