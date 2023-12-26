from codecs import decode
from Crypto.Cipher import AES


def decrypt(hex_string: str, aes_key: bytes, iv: bytes) -> bytes:
    enc = decode(hex_string, 'hex')
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    return cipher.decrypt(enc)


if __name__ == '__main__':
    flag = 'FEFAF3C16ACE95C26072B9425DAA94923053E310345F6ECDEE0820DF72DADCBD9F2A0283FAFED0781DE87C0034107C8A'
    key = b'1Q6PHZreF-jd6rBZeMQZ.z#1j3bb4h/%'
    iv_ = b'JHeR)jX=/aQFXm8b'
    flag = decrypt(flag, key, iv_)
    print(flag)
