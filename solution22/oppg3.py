from math import sqrt,ceil

def DLP(p,alpha,beta):
    m = ceil(sqrt(p))
    L1=[]
    L2=[]

    for j in range(0,m):
        L1.append(pow(alpha,m*j,p))
    # for i in range(0,m-1):
        # L2.append(pow(beta*alpha,-i,p))


    for i in range(len(L1)):
        print("{}".format(L1[i]))
        # for j in range(len(L2)):
            # print()






DLP(p=53, alpha=21, beta=26)
