# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:58:16 2020
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from
ORFs of s. Strings can be returned in any order.
@author: Jess
"""
forward = ''
with open("rosalind_orfs.txt", "r") as file:
    # print(file.read())
    for line in file.readlines():
        if not line.startswith(">"):
            forward = forward + line.replace("\n", "")
# print(forward[2])

stop = ['TAG', 'TGA', 'TAA']  # stop codons
orfcoords = []  # list for adding orf indeces to
orfseqs = []  # list of ORF seqs
sequences = [forward]  # list ready for forward and reverse seqs

rev = ""  # make the reverse complement of forward
for i in forward:
    if i == "A":
        i = "T"
    elif i == "T":
        i = "A"
    elif i == "G":
        i = "C"
    elif i == "C":
        i = "G"
    rev = rev+i
sequences.append(rev[::-1])

for seq in sequences:
    for i in range(0, len(seq)):
        if seq[i:i+3] == 'ATG':
            for j in range(i, (len(seq)), 3):
                if seq[j:j+3] in stop:
                    orfseqs.append(seq[i:j+3])
                    orfcoords.append([i, j])
                    break
                      
# print(orfcoords)
# print(orfseqs)

codon_dict = {}
with open("codon_table_list_2.txt", "r") as codonlist:
    for line in codonlist:
        col = line.split()
        codon_dict[col[0]] = col[1]

proteinlist = []
for openframe in orfseqs:
    protein = ""
    for i in range(0, len(openframe), 3):
        codon = openframe[i:i+3]
        aminoacid = codon_dict[codon]
        protein = protein + aminoacid
    proteinlist.append(protein.replace("*", ""))
print('\n'.join(set(proteinlist)))  # set uniques the list

