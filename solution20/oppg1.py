def sqr_n_mult(x,c,n):
    z = 1
    l = bin(c)[2:]
    for i in range(len(l)):
        z = z ** 2
        if (l[i:i+1] == '1'):
            z = z * x
    return z % n


if __name__ == '__main__':
    print("23^27 (mod 89) \t\t= {}  \t(tester: {})".format(sqr_n_mult(23, 27, 89),(23 ** 27) % 89))
    print("23^122 (mod 89) \t= {}  \t(tester: {})".format(sqr_n_mult(23, 122, 89),(23 ** 122) % 89))
    print("17^84 (mod 93) \t\t= {}  \t(tester: {})".format(sqr_n_mult(17, 84, 93),(17 ** 84) % 93))
    print("2991^388 (mod 5912) \t= {}  \t(tester: {})".format(sqr_n_mult(2991, 388, 5912),(2991 ** 388) % 5912))
