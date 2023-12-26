# robots not allowed
![](9b77574c71d22a1d39d7455850eb5b00)

Jak sam tytuł i opis podpowiada należy sprawdzić plik "robots.txt" na serwerze. Po wykonaniu `curl challenges.wsi.edu.pl:5003/robots.txt` pojawia się:
```
User-agent: *
Disallow: /admin
Disallow: /hidden
Disallow: /internal
Disallow: /private
Disallow: /0b0f1f9f-95b6-4fa6-b128-1b224b0864d9
Disallow: /restricted
Disallow: /confidential
Disallow: /classified
Disallow: /sensitive
Disallow: /topsecret
Disallow: /forbidden
```

Linia zawierająca UUID wyróżnia się spośród innych. Po wykonaniu `curl challenges.wsi.edu.pl:5003/0b0f1f9f-95b6-4fa6-b128-1b224b0864d9` pojawia się flaga.

Flaga: `WSIZ{isaidrobotsnotallowed!}`