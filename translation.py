# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 23:48:41 2019

@author: Jess
"""

file = open("codon_table_list.txt", "r")
codon_dict = {}
for line in file:
    col = line.split()
    codon_dict[col[0]] = col[1]

mrna = open("rosalind_prot.txt", "r")

for seq in mrna:
    protein = ""
    seq = seq.strip()
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        aminoacid = codon_dict[codon]
        protein = protein + aminoacid
    print (protein)
file.close()        