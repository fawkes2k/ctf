def encrypt(letters, key):
    return [chr((ord(l) - key) % 256) for l in letters]

nflag = ['\x93', '\x8f', '\x85', '\x96', '·', '~', ']', 'ª', '~', ']', 'ª', '~', ']', 'ª', '³', 'p', '¨', '§', '¹']
print("".join(encrypt(nflag, 60)))