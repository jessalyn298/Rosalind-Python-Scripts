# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:13:15 2019

@author: Jess
"""

file = open("rosalind_cons.txt", "r")

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
    
listofseqs = list(seq_dict.values())

countA = [0] * len(listofseqs[0])
countC = [0] * len(listofseqs[0])
countG = [0] * len(listofseqs[0])
countT = [0] * len(listofseqs[0])

finalstring = ""
for index in range(0, len(listofseqs[0])):
    for seq in listofseqs:
        if seq[index].upper() == "A":
            countA[index] += 1
        elif seq[index].upper() == "C":
            countC[index] += 1
        elif seq[index].upper() == "G":
            countG[index] += 1 
        elif seq[index].upper() == "T":
            countT[index] += 1
    
    values = [countA[index],countC[index], countG[index], countT[index]]
    if countA[index] == max(values):
        finalstring += "A"
    elif countC[index] == max(values):
        finalstring += "C"
    elif countG[index] == max(values):
        finalstring += "G"
    elif countT[index] == max(values):
        finalstring += "T"

print(finalstring)            
print("A:", " ".join(map (str, countA)))
print("C:", " ".join(map (str, countC)))
print("G:", " ".join(map (str, countG)))
print("T:", " ".join(map (str, countT)))

file.close()