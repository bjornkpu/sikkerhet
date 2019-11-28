ENC_message = 'OVM'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

for shift in range(len(ALPHABET)):
    DEC_message = ''
    for i in range(len(ENC_message)):
        for j in range(len(ALPHABET)):
            #print("{}   {}".format(ENC_message[i],ALPHABET[j]))
            if ENC_message[i] == ALPHABET[j]:
                #print("match!")
                DEC_message += ALPHABET[(j+shift)%29]
                break
    print("Shift: {}  msg: {}".format(shift,DEC_message))


print("\nDe som gjir mening på norsk er:\n TÆR, VÅT")
