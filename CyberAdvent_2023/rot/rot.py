def encrypt(plaintext: str, char_range: range, shift: int) -> str:
    length = char_range.stop - char_range.start
    return ''.join([chr((ord(c) + shift) % length + char_range[0]) for c in plaintext])


def decrypt(encrypted_text: str, char_range: range) -> dict[int: str]:
    length = char_range.stop - char_range.start
    return {i: encrypt(encrypted_text, char_range, length - i) for i in range(1, length)}


if __name__ == '__main__':
    CHAR_RANGE = range(ord(' '), ord('~'))
    text = "($x+LDP>n=b0b?4CJAEP@?N"
    decrypted = decrypt(text, CHAR_RANGE)
    for a_shift, shifted_text in list(decrypted.items()):
        if shifted_text.startswith('WSIZ'): print(a_shift, shifted_text)
