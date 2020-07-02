# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:24:20 2019
Wascally wabbits.
@author: Jess
"""
file = open("rosalind_rabbits.txt", "r")
info = file.read().split(" ")
n = int(info[0])  # number of months
k = int(info[1])  # months until death
rabbits = [1, 1]
for months in range(2, n):
    ofage_pop = int(rabbits[months-2])
    new_pop = (ofage_pop * 2) + int(rabbits[months-1]) - int(rabbits[months-k-1])
    rabbits.append(new_pop)
print(rabbits)
file.close()
