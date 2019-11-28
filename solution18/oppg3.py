index_to_char = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Æ','Ø','Å']
char_to_index = dict((char, i) for i, char in enumerate(index_to_char))

z = 17

def e_z(x):
    for i in range(len(x)):
        c = char_to_index[i]
        print(char_to_index[c])

    #(x + z) % 29
    pass


print("formelsamling => {}".format(e_z("FORMELSAMLING")))
