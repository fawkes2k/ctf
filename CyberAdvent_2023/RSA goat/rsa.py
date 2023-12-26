def create_table(n: int, e: int): return {str(pow(c, n, e)).zfill(4): c for c in range(33, 127)}


def decrypt(n: int, e: int, encrypted: str):
    res = ''
    table = create_table(n, e)
    for i in range(0, len(encrypted), 4):
        part = encrypted[i:i+4]
        char = chr(table.get(part))
        res += char
    return res



n_ = 7
e_ = 3233
t = '12981825028614352868107718251317225430200567225430521818179728722254292012971762225407313183129722542872302028722254302017621882'
print(decrypt(n_, e_, t))