# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:31:50 2020

@author: Jess
Find the Most Frequent Words in a String:
Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).
"""
info = []  # get info from file
with open("rosalind_frequentkmer.txt", "r") as file:
    info = file.readlines()
pattern = info[0].strip()  # assign info to variables from list of lines
kmerlen = int(info[1].strip())
# print(kmerlen, pattern)

kmer_dict = {}
for i in range(0, len(pattern)):
    kmer = pattern[i:i+kmerlen]
    if kmer in kmer_dict and len(pattern[i:i+kmerlen]) == kmerlen:
        kmer_dict[kmer] = kmer_dict[kmer] + 1
    else:
        kmer_dict[kmer] = 1
# print(kmer_dict)

longest_kmer = max(kmer_dict, key=kmer_dict.get)
longest_kmer_len = kmer_dict[longest_kmer]
# print(longest_kmer)

# make it return all kmers with longest kmer.
for key, value in kmer_dict.items():
    if value == longest_kmer_len:
        print(key)
