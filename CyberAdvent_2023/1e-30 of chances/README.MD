# 1e-30 of chances
![](c4eb40b31b64c2331c575ec21bc66f64)

W pliku można znależć zaszytą stronę z którą aplikacja się komunikuje oraz API, z którego korzysta:

```    http://challenges.wsi.edu.pl:5010
. /create
. /check?id= &guess= &index= 1
. /flag?id= &checksum=
```
Sprawdzając te API, można odkryć, że `/create` tworzy nową grę i zwraca jej id.

`/check` sprawdza, czy wprowadzona przez użytkownika liczba jest prawidłowa (zwraca `0` albo `1`), ale API nie blokuje gry po błędnej odpowiedzi.

`/flag` zwraca flagę po ukończeniu gry. Aby poznać algorytm tworzenia sumy kontrolnej należy zdekompilować kod binarki.

Funkcja `calculate_checksum()` tworzy ciąg znaków z odpowiedzi i wylicza hash sha256 z niego.
Po uzyskaniu odpowiedzi poprzez brute-force, wyliczeniu sumy kontrolnej i wysłanie zapytania, API zwraca flagę.

Kod: `game.py`

Flaga: `WSIZ{gue77ing_games_are_always_fun}`