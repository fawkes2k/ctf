from base64 import b64decode


def encrypt(text, key):
    t_len = len(text)
    text = bytearray(text)

    for j in range(t_len):
        for i in range(t_len):
            right = ord(key[(i + j) % len(key)])
            left = text[i] ^ right
            text[i] = left
    return text.decode()


a = b64decode('RF5NQGhod3N+YnZqTGRbfmFsbEVnbGxuTHlrdEx+bUVhYnxFdGNtaWFocn9hcA==')
print(encrypt(a, 'WSIZ'))
