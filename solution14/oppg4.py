import numpy as np
import pandas as pd

index_to_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']
char_to_index = dict((char, i) for i, char in enumerate(index_to_char))

index_to_char= [None]*30

# >4%
# E, T, R, S, N, A, I, L, O


index_to_char[23] = 'S'
index_to_char[15] = 'E'
index_to_char[17] = 'N'
index_to_char[28] = 'D'
index_to_char[29] = 'T'

index_to_char[26] = 'R'

mld = [23,1,9,15,26,7,21,17,5,21,3,15,2,6,3,29,26,14,29,5,21,7,23,15,17,28,29,20,15,17,22,15,26,20,14,23,15,9,15,29,2,6,3,23,15,17,28,29]
print(pd.DataFrame(np.bincount(mld, minlength=1),dtype='int'))

ut = []
for key, i in enumerate(mld):
    if index_to_char[i] != None:
        ut.append(index_to_char[i])
    else:
        ut.append(mld[key])

def stringify(x):
    for key, i in enumerate(x):
        x[key] = str(i)
    return x
print(ut)
