ALPHABET = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ "
melding = "Gå til Per i Hagen"
key = "eple"
enc_msg = ""

def find_place(char):
    for i in range(len(ALPHABET)):
        if char == ALPHABET[i]:
            return i

for i in range(len(melding)):
    msg_pos = find_place(melding[i])
    key_pos = find_place(key[i % len(key)])

    enc_msg += ALPHABET[(msg_pos+key_pos) % len(ALPHABET)]

print("Original msg: {}\nEncoded msg: {}".format(melding,enc_msg))


oppgB = "\n\
Hvis vi lar m = 7, så blir nøkkelen på 7 tegn. Siden vi har 59 valg \
(stor, små og mellomrom) for hvert av disse tegnene, blir det 59^7 = {} nøkler\
".format(59 ** 7)
print(oppgB)
