from math import log
p = 19
a = 5
alpha = 13
beta = 14
k = 4
#p = 29
#a = 8
#alpha = 11
#beta = 16
#k = 3


def krypter(x):
    return ((alpha ** k) % p, (x * (beta ** k)) % p)

def dekrypter(x,y):
    # TODO:
    #return (y * modinv(x**a,p)) % p
    return (y*pow(x**a,p-2,p)%p)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


melding = 17
kryptert = krypter(melding)
print("Melding: {}".format(melding))
print("Krypter {} = {}".format(melding,kryptert))

print("Dekrypter {} = {}".format(kryptert,dekrypter(kryptert[0],kryptert[1])))
