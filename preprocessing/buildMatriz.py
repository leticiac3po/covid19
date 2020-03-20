# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:01:07 2020

@author: ldhon
"""
import numpy as np

"""
    sequence is a list of numbers from 1 to 4
    
    @return nd.array (4,4)
              columns           
            _____|_____
            1  2  3  4
     |   1  
     |   2
rows-|   3
     |   4
"""
def buildMatriz(sequence, normalize=True):
    acc = {11: 0, 12: 0, 13: 0, 14:0,
           21: 0, 22: 0, 23: 0, 24:0,
           31: 0, 32: 0, 33: 0, 34:0,
           41: 0, 42: 0, 43: 0, 44:0 }
    prev_seq = sequence[0]
    for seq in sequence[1:]:
        key = prev_seq*10 + seq
        acc[key] += 1
        prev_seq = seq
    
    acc = np.fromiter(acc.values(), dtype=float).reshape(4,4)
    
    if normalize:
        acc /= np.max(acc)
    
    return acc


        
sequence = [1,2,3,4,4,3,2,1,1,2,3,4]
count = buildMatriz(sequence, False)
print(count)
