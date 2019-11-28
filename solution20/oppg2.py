from oppg1 import sqr_n_mult
p = 263
q = 401
p_b = bin(p)[2:]
q_b = bin(q)[2:]
n = p * q
on = (p-1)*(q-1)

a = 551
b = 951

melding = x = 42
print("Melding = {}".format(melding))

print("e_K(x) = x^b (mod n) => {}".format(sqr_n_mult(x,b,n)))

y = sqr_n_mult(x,b,n)
print("d_K(y) = y^a (mod n) => {}".format(sqr_n_mult(y,a,n)))


print("\n====================\n\
p:\t{}\nq:\t{}\np_b:\t{}\nq_b:\t{}\nn:\t{}\non:\t{}\nb:\t{}\na:\t{}\n\
====================".format(p,q,p_b,q_b,n,on,b,a))
