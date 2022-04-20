# B01 - Cipher

def countLen(line):
    count = 0
    for word in line:
        count = count + 1
    return count

def hurufKecil(word):
    return (97 <= ord(word) <= 122)

def hurufBesar(word):
    return (65 <= ord(word) <= 90)

def angka(word):
    return (48 <= ord(word) <= 57)

def keyGenerator(line):
    key = countLen(line)
    if key > 8:
       while key > 8: 
           key = (key % 10) + 1
    return key

def encript(line,key):
    new_string = ""
    for word in line:
        c = ord(word) + key
        if hurufKecil(word):
            if c > 122:
                c = 96 + (c - 122)
        elif hurufBesar(word):
            if c > 90:
                c = 64 + (c - 90)
        elif angka(word):
            if c > 57:
                c = 47 + (c - 57)
        else: # not (hurufKecil(word) or hurufBesar(word) or angka(word))
            c = ord(word)
        new_string = new_string + chr(c)
    return new_string

def decrypt(line,key):
    new_string = ""
    for word in line:
        c = ord(word) - key
        if hurufKecil(word):
            if c < 97:
                c = 123 - (97 - c)
        elif hurufBesar(word):
            if c < 65:
                c = 91 - (65 - c)
        elif angka(word):
            if c < 48:
                c = 58 - (48 - c)
        else: # not (hurufKecil(word) or hurufBesar(word) or angka(word))
            c = ord(word)
        new_string = new_string + chr(c)
    return new_string