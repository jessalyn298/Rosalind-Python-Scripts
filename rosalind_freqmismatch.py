# -*- coding: utf-8 -*-
"""
Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.
"""
info = []  # get info from file
with open("rosalind_freqmismatch.txt", "r") as file:
    info = file.readlines()
seq = info[0].strip()  # assign info to variables from list of lines
kmer_len = int(info[1].split()[0])
mismatches = int(info[1].split()[1])
# print(seq, kmer, mismatches)

dict_of_kmers = {}
for i in range(0, len(seq)):
    print(seq[i:i+kmer_len])