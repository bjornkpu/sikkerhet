import numpy as np
import pandas as pd

def multiplikasjonstabell(k):
    arr = np.zeros((k,k));
    for i in range(k):
        for j in range(k):
            arr[i][j] = (i*j) % k;
    arr = pd.DataFrame(arr, dtype='int')

    return arr

def invers(k):
    arr = []
    for a in range(1,k):
        for s in range(1,k):
            if (a*s) % k == 1:
                arr.append(a)
                break
    return arr

print(multiplikasjonstabell(6))
print("Multiplikative inverser: {}".format(invers(6)))
print("\n\n")
print(multiplikasjonstabell(7))
print("Multiplikative inverser: {}".format(invers(7)))
print("\n\n")
