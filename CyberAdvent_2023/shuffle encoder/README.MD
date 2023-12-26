#  shuffle encoder 
![](9433241fc16267801afff2424bf87c77)

Za pomocą narzędzia pyinstxtractor (https://github.com/extremecoders-re/pyinstxtractor) można wyeksportować pliki .pyc z binarki.
Łatwo się domyśleć, że plik  `shuffle_encoding.pyc` zawiera algorytm.
Używając narzędzia uncompyle6 (https://github.com/rocky/python-uncompyle6) można zdekomplować plik.

```
from random import seed, randrange, randint

def shuffle(array):
    i = randrange(0, len(array))
    j = randrange(0, len(array))
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp
    return array


if __name__ == '__main__':
    seed(3746435)
    message = input('Get me msg to encode: ')
    key = [randint(0, 255) for _ in range(32)]
    encoded = [hex(ord(x) ^ key[(i % len(key))]) for i, x in enumerate(message)]
    for _ in range(0, 1000):
        encoded = shuffle(encoded)

    print(''.join(map(str, encoded)))
```

Napisałem kod odwracający powyższy algorytm, który zwraca flagę.

Kod odwracający algorytm: `reversed.py`

Flaga: `WSIZ{c43s4r_w0uld_k1ll_f0r_th1s_3nc0d3r}`