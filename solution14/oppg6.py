import numpy as np

# a og m må være relativt primske. Altså må gcd være 1
m = 30
res = []
for a in range(1,m+1):
    if np.gcd(a,m) != 1:
        if a%2!=0:
            res.append(a)
print(res)
