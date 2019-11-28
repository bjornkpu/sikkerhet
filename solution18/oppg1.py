# Elementer i Z_7 1, 2, 3, 4, 5, 6, 7

Z = 7

def find_orden(element):
    i = 1
    while 1:
        if element ** i % Z == 1: return i
        i += 1

for el in range(1,Z):
    print("Element: {}, orden: {}".format(el,find_orden(el)))
