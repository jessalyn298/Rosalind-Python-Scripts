# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:50:35 2019

Fond where a query substring matches identically in a sequence string and 
return the index of that match.

@author: Jess
"""

file = open("rosalind_subs.txt", "r")
listoflists = []
for seq in (file.read().splitlines()):
    listofbases = []
    for base in seq:
        listofbases.append(base)
    listoflists.append(listofbases)
seq = listoflists[0]
query = listoflists[1]

window = len(query)
for index in range(0, len(seq)):
    if seq[index: index+window] == query:
        print(index+1)

file.close()