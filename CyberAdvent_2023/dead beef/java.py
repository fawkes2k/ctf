def parse_words(inp: str) -> str: return inp.replace(' ', '').lower()

if __name__ == '__main__':
    flag_str = '120845924642471180763985106621972535675983433142094716228248122917796888997690902594942837227041624449325891186624663848225272220295710222166557850319216542413'
    keys = [0xbad, 0xface, 0xdead, 0xbeef, 0xbed, 0xfade, 0xcab, 0xfed, 0xbead]
    flag = int(flag_str)
    for key in keys: flag ^= key
    flag //= (int(parse_words('Bad Face'), 16)**2)
    flag //= (int(parse_words('Dead Beef'), 16)**2)
    print(flag.to_bytes(51).decode())
