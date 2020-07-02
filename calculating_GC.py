# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:48:52 2019

Calculate GC content of sequences in a FASTA file and return the highest GC 
content.

@author: Jess
"""

#with open("rosalind_input.txt", "r") as file:
file = open("rosalind_gc.txt", "r")
seq_dict = {}
for line in file:
    line = line.strip()
    if line == "":
        continue
    if line[0] == ">":
        seq_dict[line] = ""
        last_seq = line
    else:
        seq_dict[last_seq] += line 
#        if seq_dict[last_seq] == "":
#            seq_dict[last_seq] = line
#        else:
#            seq_dict[last_seq] += line
GC_dict = {}
for seq_name in seq_dict:
    GC_cont = 0
    GC = 0
    for base in seq_dict[seq_name]:
        if base.upper() == "C" or base.upper() == "G":
            GC += 1
    GC_cont = (GC / len(seq_dict[seq_name])) * 100
    GC_dict[seq_name] = GC_cont

max_GC = max(GC_dict.values())
for seq_name in GC_dict:
    if GC_dict[seq_name] == max_GC:
        print(seq_name, max_GC)
file.close()