from math import sqrt,ceil
# aplha = 70
# beta = 2
# p = 131
alpha = 21
beta = 26
p = 53

print(pow(alpha,p,p))


m = ceil(sqrt(p))
print("m = {}".format(m))

L1 = []
L2 = []

for i in range(0,m):
    value = pow(alpha,m * i,p)
    L1.append((i,value))

for j in range(0,m):
    value = (beta * pow(alpha,p-j,p)) % p
    L2.append((j,value))

print(sorted(L1, key=lambda x:x[0]))
print(sorted(L2, key=lambda x:x[0]))

x1,x2 =0,0

for r in L1:
    for t in L2:
        if r == t:
            x1 = L1.index(r)
            x2 = L2.index(t)
            print(x1,x2)
            break


print('the value of x is ', ((x2+1)*m - x1) % p) # Answer
