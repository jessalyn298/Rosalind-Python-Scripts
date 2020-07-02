# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:25:46 2019
Mendelian inheritance
@author: Jess
"""
file = open("rosalind_iprb.txt", "r")
info = file.read().split()
k_dominant = int(info[0])
m_hetero = int(info[1])
n_recessive = int(info[2])

k_k = sum(range(1, k_dominant))
m_m = sum(range(1, m_hetero))
n_n = sum(range(1, n_recessive))
k_m = k_dominant * m_hetero
k_n = k_dominant * n_recessive
m_n = m_hetero * n_recessive
total = k_k + m_m + n_n + k_m + k_n + m_n

Pdominant = (k_k + k_m + k_n + (0.5 * m_n) + (0.75 * m_m)) / total

print(Pdominant)
 

file.close()
