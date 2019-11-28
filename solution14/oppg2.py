ENC_message = 'NDQVNMHNRPPHUNRQJHQ'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'


DEC_message = ''
for i in range(len(ENC_message)):
    for j in range(len(ALPHABET)):
        #print("{}   {}".format(ENC_message[i],ALPHABET[j]))
        if ENC_message[i] == ALPHABET[j]:
            #print("match!")
            DEC_message += ALPHABET[j+3]
            break
print("Encoded msg: {}\nDecoded msg: {}".format(ENC_message,DEC_message))
