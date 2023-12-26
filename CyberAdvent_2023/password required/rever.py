def xor(text, key):
    result = ''
    for i in range(len(text)):
        result += chr(ord(key[i % len(key)]) ^ ord(text[i]))
    return result


a = '16110a1e3a7221223431202535732c2a1e2c73301e2c707725272739'
b = ''.join([chr(int(a[i:i+2], 16)) for i in range(0, len(a), 2)])
d = xor(b, 'ABCD')
print(d)