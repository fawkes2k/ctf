# jwt adventure
![](2cd1f1fa22787ad1ff06c9430933b1c4)

Po otworzeniu strony pojawia się prosta strona z polem do wpisania nazwy użytkownika. Po wpisaniu nazwy i kliknięciu "Log in" pojawia się wiadomość:
```

Hello 32r.

You must be an admin to continue your adventure...
```

Sprawdziłem wysłane przez przeglądarkę zapytania. Po kliknięciu przycisku, wysyła zapytanie POST do `/login`, które ustawia ciasteczko z id sesji i token oraz przekierowuje do `/me`.
Tak jak sam tytuł i opis mówią, token ten to JSON Web Token.
Dane z odkodowanego tokenu to  `{ "username": "32r", "admin": false}`. Oczywiste wydaje się wysłanie zapytania do `/me` z zmodyfikowanym tokenem, w którym wartość "admin" jest ustawiona na "true".

Po wysłaniu zapytania `curl 'http://challenges.wsi.edu.pl:5012/me' -H 'Cookie: session=eyJpZCI6Mn0.ZXQmmQ.8RNS7Rcurzc0yyHVVpSzH3SoL1o; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjMyciIsImFkbWluIjp0cnVlfQ.QVu_MpdUcJrR_cD4i7ffZLyRclSyr488IO0gp4K7OQY'` pojawia się strona z flagą.


Program odkodowujący i zmieniający token: `jwt_adv.py`
Flaga: `WSIZ{a1g_n0ne_1s_the_n3w_bl4ck}`