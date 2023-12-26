from random import seed, randrange, randint


def unshuffle(array, aaa):
    i, j = aaa
    tmp = array[j]
    array[j] = array[i]
    array[i] = tmp
    return array


if __name__ == '__main__':
    seed(3746435)
    message = '0x7d0x1d0x820xed0x5b0x510x9b0xa90x880xcb0x950x6a0x7c0xae0xe80x8e0xaf0x770xcc0xe10xa30x590xa20x200xfa0x750x630x8a0xe20x890x760x2d0x250xa90x690xdf0x10x900x2c0x6a'.split('0x')[1:]
    key = [randint(0, 255) for _ in range(32)]
    aa = [(randrange(0, len(message)), randrange(0, len(message))) for _ in range(0, 1000)]
    aa.reverse()
    for i in range(0, 1000): message = unshuffle(message, aa[i])
    encoded = [chr(int(x, 16) ^ key[i % len(key)]) for i, x in enumerate(message)]
    print(''.join(encoded))
